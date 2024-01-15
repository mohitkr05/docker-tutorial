# Docker inspect 

```bash
$ docker inspect 

[
    {
        "Id": "441adc0ccd4a729ce6bde148664bed9675db656a1381ad806296a739b048f7f1",
        "Created": "2024-01-13T11:40:51.026748754Z",
        "Path": "/docker-entrypoint.sh",
        "Args": [
            "nginx",
            "-g",
            "daemon off;"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 18125,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2024-01-13T11:40:53.737015925Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:a8758716bb6aa4d90071160d27028fe4eaee7ce8166221a97d30440c8eac2be6",
        "ResolvConfPath": "/var/lib/docker/containers/441adc0ccd4a729ce6bde148664bed9675db656a1381ad806296a739b048f7f1/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/441adc0ccd4a729ce6bde148664bed9675db656a1381ad806296a739b048f7f1/hostname",
        "HostsPath": "/var/lib/docker/containers/441adc0ccd4a729ce6bde148664bed9675db656a1381ad806296a739b048f7f1/hosts",
        "LogPath": "/var/lib/docker/containers/441adc0ccd4a729ce6bde148664bed9675db656a1381ad806296a739b048f7f1/441adc0ccd4a729ce6bde148664bed9675db656a1381ad806296a739b048f7f1-json.log",
        "Name": "/admiring_lumiere",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {},
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "ConsoleSize": [
                30,
                120
            ],
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "host",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
            "BlkioDeviceWriteBps": [],
            "BlkioDeviceReadIOps": [],
            "BlkioDeviceWriteIOps": [],
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": false,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/023f1f7e964ddfee610f7d7b4bb3e779b9b66ecaabe17a3edc49383581ebe0b5-init/diff:/var/lib/docker/overlay2/198873f8ffe58c733cc1a60de65a9998ee700eb0072e0cb0d7c555b972570ff2/diff:/var/lib/docker/overlay2/b708ea6d22edce7be4c4f3b26b3284a952818d71ee758e5e47cf3877f8e23824/diff:/var/lib/docker/overlay2/5bd5c67cc664f7174d8e78b173d8b20ffd14ef25380a7d528162833e7b28d689/diff:/var/lib/docker/overlay2/071008b2b823c89a473666ea7878507246927f2ce28f8a6163592a31a7c338ab/diff:/var/lib/docker/overlay2/e156cb6a19b8637994016e53ce9eeac94c32622c7bc22d8a56debd7bd06fccba/diff:/var/lib/docker/overlay2/56fa3a14f5d906eaedc1b34d76310d2979a4e8e8100a13081df983aa18e3fe7a/diff:/var/lib/docker/overlay2/347402b674bcbb59837ed922c8d7e47529811b4a7b9897e911ac8422529b0eb6/diff",
                "MergedDir": "/var/lib/docker/overlay2/023f1f7e964ddfee610f7d7b4bb3e779b9b66ecaabe17a3edc49383581ebe0b5/merged",
                "UpperDir": "/var/lib/docker/overlay2/023f1f7e964ddfee610f7d7b4bb3e779b9b66ecaabe17a3edc49383581ebe0b5/diff",
                "WorkDir": "/var/lib/docker/overlay2/023f1f7e964ddfee610f7d7b4bb3e779b9b66ecaabe17a3edc49383581ebe0b5/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "441adc0ccd4a",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": true,
            "AttachStderr": true,
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "NGINX_VERSION=1.25.3",
                "NJS_VERSION=0.8.2",
                "PKG_RELEASE=1~bookworm"
            ],
            "Cmd": [
                "nginx",
                "-g",
                "daemon off;"
            ],
            "Image": "nginx:latest",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": [
                "/docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {
                "maintainer": "NGINX Docker Maintainers \u003cdocker-maint@nginx.com\u003e"
            },
            "StopSignal": "SIGQUIT"
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "8544780d9d2b12d7c8271e8fa2c84fbe1d4d2d97fe4beee356025e50f16ad9a3",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/8544780d9d2b",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "bdf59860b37b6409ecf6325f6adf15902b4f0b505ab5b4224788160e4ad5329d",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:02",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "c5491bfa19d9b403705dd52577e4b68b01658b3636c5035eb6b65409d2e0f190",
                    "EndpointID": "bdf59860b37b6409ecf6325f6adf15902b4f0b505ab5b4224788160e4ad5329d",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:02",
                    "DriverOpts": null
                }
            }
        }
    }
]

```