import enum
import inspect
import typing

import zodchy
import functools

AuthRoleType = typing.TypeVar("AuthRoleType", bound=enum.Enum)


class AuthContext:
    pass


class AuthPolicy(enum.Enum):
    ALLOW = enum.auto()
    DENY = enum.auto()


class AuthAuditor:
    def __init__(
        self,
        access_deny_exception: type[zodchy.codex.cqea.Error],
        policy: AuthPolicy = AuthPolicy.DENY,
    ):
        self._access_deny_exception = access_deny_exception
        self._policy = policy

    def __call__(self, *roles: AuthRoleType, policy: AuthPolicy | None = None):
        policy = policy or self._policy

        def wrapper(func):
            sign = inspect.signature(func)
            for param in sign.parameters.values():
                if AuthContext in param.annotation.__mro__:
                    auth_context_field_name = param.name
                    break
            else:
                auth_context_field_name = "auth_context"
                param = inspect.Parameter(
                    auth_context_field_name,
                    inspect.Parameter.POSITIONAL_OR_KEYWORD,
                    annotation=AuthContext,
                )
                params = list(sign.parameters.values())
                params.append(param)
                sign = sign.replace(parameters=params)

            @functools.wraps(func)
            def inner(*args, **kwargs):
                auth_context = kwargs.get(auth_context_field_name)
                if not auth_context:
                    return self._access_deny_exception()
                if (
                    auth_context.roles & set(roles) == set()
                    and policy == AuthPolicy.DENY
                ):
                    return self._access_deny_exception()
                return func(*args, **kwargs)

            inner.__signature__ = sign
            return inner

        return wrapper
