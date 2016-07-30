from iauctb_py import wrapper
import config

iauctb = wrapper.IAUCTB(config.Username, config.Password)
iauctb.login()