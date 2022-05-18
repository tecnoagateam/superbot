from homebot import get_config
from homebot.core.logging import LOGI

def user_is_admin(user_id):
	"""
	Check if the given user ID is in the list
	of the approved user IDs.
	"""
	if str(user_id) not in get_config("CI_APPROVED_USER_IDS").split():
		LOGI(f"İstifadəçiyə giriş rədd edildi {user_id}")
		return False

	LOGI(f"İstifadəçiyə giriş {user_id}")
	return True
