(function(){
    $.atoms.self_server_get_dfusage = [
        {
            tag_code: "self_server_ip",
            type: "input",
            attrs: {
                name: "主机IP",
                hookable: true,
                default: '10.0.1.192',
                validation: [
                    {
                        type: "required"
                    }
                ]
            },
        },
        {
            tag_code: "self_server_system",
            type: "radio",
            attrs: {
                name: "主机系统",
                items: [
                    {value: "1", name: "linux centos"},
                    {value: "2", name: "Windows"},
                    {value: "3", name: "linux ubuntu"},
                ],
                default: "1",
                hookable: true,
                validation: [
                    {
                        type: "required"
                    }
                ]
            }
        },
        {
            tag_code: "self_server_disk",
            type: "input",
            attrs: {
                name: "主机磁盘",
                hookable: true,
                default: '/',
                validation: [
                    {
                        type: "required"
                    }
                ]
            },
        },
    ]
})();