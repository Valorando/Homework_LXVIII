from fastapi import FastAPI, Request, status, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import ValidationError
from fastapi.responses import JSONResponse
from loguru import logger
from TradeAPI.Models.InputOutputModel import IOModel
from TradeAPI.Models.EditModel import EModel
from TradeAPI.DI_Container.ITradeService_TradeService_binding import trade_service
import time
import os

log_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'TradeAPI', 'Logs', 'trade_api_log.log'))

logger.add(log_file_path, format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}", rotation="1 day")

app = FastAPI(title="Trading Api")

@app.on_event("startup")
async def startup_event():
    logger.info("Starting Trading API...")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down Trading API...")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    request_time = time.time()
    logger.info(f"Request from {request.client.host}: {request.method} {request.url}")
    response = await call_next(request)
    process_time = time.time() - request_time
    logger.info(f"Response status code: {response.status_code} - Processed in {process_time:.4f} seconds")
    return response

@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    logger.error(f"Validation error: {exc.errors()}")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )

@app.get("/orders/")
def get_orders():
    orders = trade_service.Get_all_orders()
    logger.info(f"Fetched orders: {orders}")
    return orders

@app.post("/orders/")
def create_order(order: IOModel):
    try:
        logger.info(f"Creating order with data: {order}")
        trade_service.Add_order(order)
    except Exception as e:
        logger.error(f"Error creating order: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
    logger.info(f"Order successfully added: {order}")
    return "Order successfully added"

@app.put("/orders/{order_id}")
def update_order(order_id: int, order: EModel):
    try:
        logger.info(f"Updating order {order_id} with data: {order}")
        trade_service.Edit_order(order)
    except Exception as e:
        logger.error(f"Error updating order {order_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
    logger.info(f"Order successfully updated: {order}")
    return "Order successfully updated"

@app.delete("/orders/{order_id}")
def remove_order(order_id: int):
    try:
        logger.info(f"Deleting order with ID: {order_id}")
        trade_service.Delete_order(order_id)
    except Exception as e:
        logger.error(f"Error deleting order {order_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
    logger.info(f"Order successfully deleted: {order_id}")
    return "Order successfully deleted"
