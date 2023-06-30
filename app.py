from pinferencia import Server

def model(data):
    return sum(data)

service = Server()
service.register(
    model_name="mymodel",
    model=model,
    metadata={}
)
