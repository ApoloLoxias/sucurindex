package environment

import (
	"testing"
)

func TestGetEnv_Success(t *testing.T) {
	env, err := GetEnv()
	if err != nil {
		t.Fatalf("GetEnv() returned error: %v", err)
	}

	expectedHost := "724339dd-4b74-486c-a5b4-b95907e4915d"
	if env.CurrentHost != expectedHost {
		t.Errorf("CurrentHost = %q, want %q", env.CurrentHost, expectedHost)
	}

	expectedPath := "/home/wsluser/code_projects/personal/sucurindex/sucurindex/metadata/"
	if env.MetadataStoragePath != expectedPath {
		t.Errorf("MetadataStoragePath = %q, want %q", env.MetadataStoragePath, expectedPath)
	}
}
