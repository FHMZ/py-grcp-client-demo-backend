import grpc

from app.controllers.grpc.proto.users import users_pb2_grpc, users_pb2


class UserService:
    def __init__(self, host: str = "localhost", port: int = 50051):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = users_pb2_grpc.UsersStub(self.channel)

    def get_all_users(self):
        """Calls the GetUser gRPC endpoint."""
        request = users_pb2.GetUsersRequest()
        response = self.stub.GetUsers(request)

        return {
            "user_id": response.user_id,
            "name": response.name,
            "email": response.email,
        }
