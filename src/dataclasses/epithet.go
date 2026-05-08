package dataclasses

type Taxon string

const (
	File       Taxon = "file"
	FileSystem Taxon = "fileSystem"
	Host       Taxon = "host"
	Machine    Taxon = "machine"
	Mount      Taxon = "mount"
	Storage    Taxon = "storage"
	Volume     Taxon = "volume"
)

type Epithet interface {
	Taxon() Taxon
}
