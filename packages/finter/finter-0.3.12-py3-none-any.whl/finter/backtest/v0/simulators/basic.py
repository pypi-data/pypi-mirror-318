from finter.backtest.core import (
    calculate_buy_sell_volumes,
    execute_transactions,
    update_nav,
    update_target_volume,
    update_valuation_and_cash,
)
from finter.backtest.v0.simulators.base import BaseBacktestor


class BasicBacktestor(BaseBacktestor):
    def run(self):
        for i in range(1, self.frame.shape[0]):
            self.vars.position.target_volume[i] = update_target_volume(
                self.weight[i],
                self.vars.result.nav[i - 1, 0],
                self.price[i - 1],
                self.weight[i - 1],
                self.vars.position.target_volume[i - 1],
                self.execution.auto_rebalance,
                i == 1,
            )

            (
                self.vars.buy.target_buy_volume[i],
                self.vars.sell.target_sell_volume[i],
                self.vars.sell.actual_sell_volume[i],
            ) = calculate_buy_sell_volumes(
                self.vars.position.target_volume[i],
                self.vars.position.actual_holding_volume[i - 1],
                volume_capacity=self.volume_capacity[i],
            )

            (
                self.vars.sell.actual_sell_amount[i],
                self.vars.buy.available_buy_amount[i, 0],
                self.vars.buy.actual_buy_volume[i],
                self.vars.buy.actual_buy_amount[i],
            ) = execute_transactions(
                self.vars.sell.actual_sell_volume[i],
                self.buy_price[i],
                self.cost.buy_fee_tax,
                self.sell_price[i],
                self.cost.sell_fee_tax,
                self.vars.result.cash[i - 1, 0],
                self.vars.buy.target_buy_volume[i],
            )

            (
                self.vars.position.actual_holding_volume[i],
                self.vars.result.valuation[i],
                self.vars.result.cash[i, 0],
            ) = update_valuation_and_cash(
                self.vars.position.actual_holding_volume[i - 1],
                self.vars.buy.actual_buy_volume[i],
                self.vars.sell.actual_sell_volume[i],
                self.price[i],
                self.vars.buy.available_buy_amount[i, 0],
                self.vars.buy.actual_buy_amount[i],
            )
            self.vars.result.nav[i, 0] = update_nav(
                self.vars.result.cash[i, 0], self.vars.result.valuation[i]
            )

        if not self.optional.debug:
            self.summary = self._summary
            self._clear_all_variables()
        else:
            self.summary = self._summary
        return self.summary
