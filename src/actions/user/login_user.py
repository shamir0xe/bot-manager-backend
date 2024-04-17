from src.helpers.state_manager import State
from src.mediators.token_mediator import TokenMediator


class LoginUser:
    @staticmethod
    def with_user_id(user_id: str) -> State:
        mediator = TokenMediator.with_user_id(user_id).check_expiration()
        if not mediator.state.is_ok:
            ## either:
                # 1) token is not set, or 
                # 2) got expired
            mediator.state = State.ok()
            mediator.revoke_token().save()
        return mediator.state
