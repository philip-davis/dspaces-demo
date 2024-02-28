c = get_config()

c.ServerApp.allow_root = True
c.LabServerApp.open_browser = False
c.ServerApp.port = 8888
c.ServerApp.preferred_dir = "/notebooks"

