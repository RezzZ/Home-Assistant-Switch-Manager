from homeassistant import config_entries

from .const import DOMAIN

@config_entries.HANDLERS.register(DOMAIN)
class SwitchManagerConfigFlow(config_entries.ConfigFlow):

    VERSION = 1

    async def async_step_user(self, user_input=None):
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")
        return self.async_create_entry(title="Switch Manager", data={})