import tomlkit
import os



def get_pstorage() -> str:
    config_path=os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "config.toml"
        )
    )

    with open(config_path) as f:
        config = tomlkit.load(f)

    return os.path.abspath(config["Persistent Storage"]["Primary Storage Directory"])
