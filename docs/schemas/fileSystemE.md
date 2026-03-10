# WSL_FS

File system for wsl.

---

## --- SucurIndex Metadata --- MboiDown :: v0.0.0 ---

### Root
vr/Users/pichau/AppData/Local/Packages/TheDebianProject.DebianGNULinux_76v4gfsz19hv4/LocalState/rootfs/
// Root is where to find the origin of the fs when mounting the volume as an external drive, "vr/" representing volume root. Follows unix forward slash path conventions. Could point to a file (i.e. a diskimage) instead of a folder.

### Mounts
[[00000000-0000-0000-0000-00000001 | C:]]<--bridge=\\wsl.localhost, GUID=uuid,> // links to mountEntry - one per mount point. Optional since external storage drives don't have persistent mount points. May have a bridge, description, for instance IP adress + port for network shares. The partition GUID is unique to the volume-mount couple and will be used as the uuid of the FS-mount link in database

### Type
NTFS_unix //Not necessarily the same type as the native filesystem_type in the volume it is attached to. I used NTFS_unix because it is ntfs, but behaves like ext4, btfs and the likes in terms of case sensitivity

---
"Serpent slithers. Sediment survives"