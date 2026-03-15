package environment

import (
	"github.com/BurntSushi/toml"
)

const envPath = "/home/wsluser/code_projects/personal/sucurindex/sucurindex/" +
	"src/environment/env.toml"

type Environment struct {
	CurrentHost         string
	MetadataStoragePath string
}

func GetEnv() (env Environment, err error) {
	_, err = toml.DecodeFile(envPath, &env)
	if err != nil {
		return Environment{}, err
	}
	return env, err
}
