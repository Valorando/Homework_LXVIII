from TradeAPI.Connect.MySQL_connect import cursor, requests_data, db
from TradeAPI.Models.InputOutputModel import IOModel
from TradeAPI.Models.EditModel import EModel
from TradeAPI.Interfaces.ITradeService import ITS

class TS(ITS):
    def Get_all_orders(self):
        cursor.execute(requests_data['Get_all_orders_request'])
        results = cursor.fetchall()
        orders = []
        for row in results:
            order = IOModel(
                id=row[0],
                user_id=row[1],
                currency=row[2],
                side=row[3],
                price=row[4],
                amount=row[5]
            )
            orders.append(order)
        return orders

    
    def Add_order(self, order: IOModel):
     cursor.execute(requests_data['Add_order_request'], (order.id, order.user_id, order.currency, order.side.value, order.price, order.amount))
     db.commit()

    def Edit_order(self, order: EModel):
     cursor.execute(requests_data['Edit_order_request'], (order.new_id, order.new_user_id, order.new_currency, order.new_side.value, order.new_price, order.amount, order.id))
     db.commit()

    def Delete_order(self, order_id: int):
     cursor.execute(requests_data['Delete_order_request'], (order_id,))
     db.commit()

