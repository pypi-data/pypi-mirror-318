from sgqlc.operation import Operation, Fragment
from sgqlc.types import Variable
from llq.schema import (
    RootMutation,
    LoginInput,
    RefreshJwtAuthTokenInput,
)
from llq.base_operation_builder import BaseOperationBuilder
from dataclasses import dataclass


@dataclass
class LoginResponse:
    auth_token: str
    refresh_token: str

    @staticmethod
    def from_dict(data: dict) -> "LoginResponse":
        """
        Parse a dictionary into a LoginResponse instance.
        """
        return LoginResponse(
            auth_token=data["auth_token"],
            refresh_token=data["refresh_token"],
        )


class LoginMutation(BaseOperationBuilder):
    """
    A builder for login-related GraphQL mutation
    """

    def get(self, input: LoginInput) -> Operation:
        op = Operation(RootMutation, name="login_user_mutation")

        user = op.login(input=input)

        user.auth_token()
        user.refresh_token()

        return op

    @staticmethod
    def parse(data: dict) -> "LoginResponse":
        return LoginResponse.from_dict(data.get("login", {}))


@dataclass
class RefreshTokenResponse:
    auth_token: str

    @staticmethod
    def from_dict(data: dict) -> "RefreshTokenResponse":
        """
        Parse a dictionary into a RefreshTokenResponse instance.
        """
        return RefreshTokenResponse(auth_token=data["auth_token"])


class RefreshTokenMutation(BaseOperationBuilder):
    """
    A builder for refresh-token-related GraphQL mutation
    """

    def get(self, input: RefreshJwtAuthTokenInput) -> Operation:
        op = Operation(RootMutation, name="refresh_token_mutation")

        token = op.refresh_jwt_auth_token(input=input)

        token.auth_token()

        return op

    @staticmethod
    def parse(data: dict) -> "RefreshTokenResponse":
        return RefreshTokenResponse.from_dict(data.get("refreshJwtAuthToken", {}))
