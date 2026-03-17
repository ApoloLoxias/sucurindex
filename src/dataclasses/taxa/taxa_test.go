package taxa

import (
	"github.com/ApoloLoxias/sucurindex/src/dataclasses"
	"github.com/google/uuid"
	"testing"
)

func TestFileE(t *testing.T) {
	id := uuid.New()
	link := dataclasses.Link{
		Source: id,
		Target: uuid.New(),
		Properties: []dataclasses.LinkProperty{
			{Name: "direction", Value: "outgoing"},
		},
	}

	file := FileE{
		ID:          id,
		Name:        "project_notes",
		Description: "My important project notes",
		Paths: []string{
			"[[uuid | hostname]]: /home/wsluser/projects/notes.md",
		},
		Links:   []dataclasses.Link{link},
		Tags:    []string{"work", "project"},
		Size:    4096,
		Mtime:   1709830800,
		Missing: false,
	}

	if file.ID != id {
		t.Errorf("ID = %v, want %v", file.ID, id)
	}
	if file.Name != "project_notes" {
		t.Errorf("Name = %q, want %q", file.Name, "project_notes")
	}
	if len(file.Paths) != 1 {
		t.Errorf("len(Paths) = %d, want 1", len(file.Paths))
	}
	if len(file.Links) != 1 {
		t.Errorf("len(Links) = %d, want 1", len(file.Links))
	}
	if len(file.Tags) != 2 {
		t.Errorf("len(Tags) = %d, want 2", len(file.Tags))
	}

	file2 := FileE{
		ID:   id,
		Name: "project_notes",
		Paths: []string{
			"[[uuid | hostname]]: /home/wsluser/projects/notes.md",
		},
		Size:    4096,
		Mtime:   1709830800,
		Missing: false,
	}

	if file2.Description != "" {
		t.Errorf("Description = %q, want not nil", file2.Description)
	}
	if file2.Links != nil {
		t.Errorf("Links not nil")
	}
	if file2.Tags != nil {
		t.Errorf("Tags not nil")
	}
}

func TestFileSystemE(t *testing.T) {
	id := uuid.New()
	mountLink := dataclasses.Link{
		Source: id,
		Target: uuid.New(),
		Properties: []dataclasses.LinkProperty{
			{Name: "bridge", Value: `\\wsl.localhost, GUID=abc123`},
		},
	}

	fs := FileSystemE{
		ID:          id,
		Name:        "WSL_FS",
		Description: "File system for wsl",
		Root:        "vr/Users/pichau/AppData/Local/Packages/...",
		Mounts:      []dataclasses.Link{mountLink},
		Type:        "NTFS_unix",
	}

	if fs.ID != id {
		t.Errorf("ID = %v, want %v", fs.ID, id)
	}
	if fs.Name != "WSL_FS" {
		t.Errorf("Name = %q, want %q", fs.Name, "WSL_FS")
	}
	if fs.Root != "vr/Users/pichau/AppData/Local/Packages/..." {
		t.Errorf("Root = %q, want %q", fs.Root, "vr/Users/pichau/AppData/Local/Packages/...")
	}
	if len(fs.Mounts) != 1 {
		t.Errorf("len(Mounts) = %d, want 1", len(fs.Mounts))
	}
	if fs.Type != "NTFS_unix" {
		t.Errorf("Type = %q, want %q", fs.Type, "NTFS_unix")
	}
}

func TestHostE(t *testing.T) {
	id := uuid.New()

	host := HostE{
		ID:          id,
		Name:        "desktop_windows",
		Description: "Windows 11 installation on desktop machine",
		OS:          "windows_11",
		HostName:    "DESKTOP-ABC123",
		Users:       []string{"wuser", "wsluser"},
	}

	if host.ID != id {
		t.Errorf("ID = %v, want %v", host.ID, id)
	}
	if host.Name != "desktop_windows" {
		t.Errorf("Name = %q, want %q", host.Name, "desktop_windows")
	}
	if host.Description != "Windows 11 installation on desktop machine" {
		t.Errorf(
			"Description = %q, want %q",
			host.Description,
			"Windows 11 installation on desktop machine",
		)
	}
	if host.OS != "windows_11" {
		t.Errorf("OS = %q, want %q", host.OS, "windows_11")
	}
	if host.HostName != "DESKTOP-ABC123" {
		t.Errorf("HostName = %q, want %q", host.HostName, "DESKTOP-ABC123")
	}
	if host.Users[0] != "wuser" || host.Users[1] != "wsluser" {
		t.Errorf("Users = %q, want %q", host.Users, []string{"wuser", "wsluser"})
	}
}

func TestMachineE(t *testing.T) {
	id := uuid.New()

	machine := MachineE{
		ID:          id,
		Name:        "desktop",
		Description: "Main desktop computer",
		Type:        "desktop",
		Location:    "My house",
	}

	if machine.ID != id {
		t.Errorf("ID = %v, want %v", machine.ID, id)
	}
	if machine.Name != "desktop" {
		t.Errorf("Name = %q, want %q", machine.Name, "desktop")
	}
	if machine.Description != "Main desktop computer" {
		t.Errorf(
			"Desription = %q, want %q",
			machine.Description,
			"New desktop computer",
		)
	}
	if machine.Type != "desktop" {
		t.Errorf("Type = %q, want %q", machine.Type, "desktop")
	}
	if machine.Location != "My house" {
		t.Errorf("Location = %q, want %q", machine.Location, "My house")
	}
}

func TestMountE(t *testing.T) {
	id := uuid.New()
	hostLink := dataclasses.Link{
		Source: id,
		Target: uuid.New(),
		Properties: []dataclasses.LinkProperty{
			{Name: "type", Value: "host_link"},
		},
	}

	mount := MountE{
		ID:          id,
		Name:        "C:",
		Description: "Windows system partition mount",
		Host:        hostLink,
		Path:        "C:\\",
	}

	if mount.ID != id {
		t.Errorf("ID = %v, want %v", mount.ID, id)
	}
	if mount.Name != "C:" {
		t.Errorf("Name = %q, want %q", mount.Name, "C:")
	}
	if mount.Description != "Windows system partition mount" {
		t.Errorf(
			"Description %q, expected %q",
			mount.Description,
			"Windows system partition mount",
		)
	}
	if mount.Host.Source != hostLink.Source ||
		mount.Host.Target != hostLink.Target ||
		len(mount.Host.Properties) != len(hostLink.Properties) {
		t.Errorf("Host %#v, want %#v", mount.Host, hostLink)
	}
	if mount.Path != "C:\\" {
		t.Errorf("Path = %q, want %q", mount.Path, "C:\\")
	}
}

func TestStorageE(t *testing.T) {
	id := uuid.New()
	machineLink := dataclasses.Link{
		Source: id,
		Target: uuid.New(),
		Properties: []dataclasses.LinkProperty{
			{Name: "type", Value: "installed_at"},
		},
	}
	volumeLink := dataclasses.Link{
		Source: id,
		Target: uuid.New(),
		Properties: []dataclasses.LinkProperty{
			{Name: "type", Value: "volume"},
		},
	}

	storage := StorageE{
		ID:           id,
		Name:         "DesktopSSD",
		Description:  "The main internal SSD for my desktop",
		MediaType:    "ssd_m2",
		Model:        "samsung SSD 874891",
		SerialNumber: "78sdayu",
		DeviceType:   "internal",
		Capacity:     1000000000000,
		InstalledAt:  machineLink,
		Volumes:      []dataclasses.Link{volumeLink},
		Location:     "My house, inside main desktop",
	}

	if storage.ID != id {
		t.Errorf("ID = %v, want %v", storage.ID, id)
	}
	if storage.Name != "DesktopSSD" {
		t.Errorf("Name = %q, want %q", storage.Name, "DesktopSSD")
	}
	if storage.MediaType != "ssd_m2" {
		t.Errorf("MediaType = %q, want %q", storage.MediaType, "ssd_m2")
	}
	if storage.Capacity != 1000000000000 {
		t.Errorf("Capacity = %d, want %d", storage.Capacity, 1000000000000)
	}
	if len(storage.Volumes) != 1 {
		t.Errorf("len(Volumes) = %d, want 1", len(storage.Volumes))
	}
}

func TestVolumeE(t *testing.T) {
	id := uuid.New()

	volume := VolumeE{
		ID:          id,
		Name:        "sda1_windows",
		Description: "Primary Windows partition on desktop SSD",
		Capacity:    200000000,
		Type:        "NTFS",
	}

	if volume.ID != id {
		t.Errorf("ID = %v, want %v", volume.ID, id)
	}
	if volume.Name != "sda1_windows" {
		t.Errorf("Name = %q, want %q", volume.Name, "sda1_windows")
	}
	if volume.Capacity != 200000000 {
		t.Errorf("Capacity = %d, want %d", volume.Capacity, 200000000)
	}
	if volume.Type != "NTFS" {
		t.Errorf("Type = %q, want %q", volume.Type, "NTFS")
	}
}
