import grpc

from app.controllers.grpc.proto.users import users_pb2_grpc, users_pb2


def run():
    response = []

    with grpc.insecure_channel('localgost:50051') as channel:
        stub = users_pb2_grpc.UsersStub(channel)
        response = stub.GetUsers(users_pb2.GetUsersRequest())

    print(response.users)


if __name__ == "__main__":
    run()
