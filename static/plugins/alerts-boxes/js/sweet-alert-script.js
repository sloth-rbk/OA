$(document).ready(function () {

    $("#alert-basic").click(function () {
        swal("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lorem erat, tincidunt vitae ipsum et, pellentesque maximus enim. Mauris eleifend ex semper, lobortis purus sed, pharetra felis");
    });

    $("#alert-title").click(function () {
        swal("Here's the title!", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lorem erat, tincidunt vitae ipsum et, pellentesque maximus enim. Mauris eleifend ex semper, lobortis purus sed, pharetra felis");
    });

    $("#alert-success").click(function () {
        swal("Good job!", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lorem erat, tincidunt vitae ipsum et, pellentesque maximus enim. Mauris eleifend ex semper, lobortis purus sed, pharetra felis", "success");
    });

    $("#alert-error").click(function () {
        swal("Somthing Wrong!", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lorem erat, tincidunt vitae ipsum et, pellentesque maximus enim. Mauris eleifend ex semper, lobortis purus sed, pharetra felis,", "error");
    });

    $("#alert-info").click(function () {
        swal("Information!", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lorem erat, tincidunt vitae ipsum et, pellentesque maximus enim. Mauris eleifend ex semper, lobortis purus sed, pharetra felis,", "info");
    });

    $("#alert-warning").click(function () {
        swal("Warning!", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lorem erat, tincidunt vitae ipsum et, pellentesque maximus enim. Mauris eleifend ex semper, lobortis purus sed, pharetra felis,", "warning");
    });

});

// sloth：
function alert_del_someb(self) {
    var csrfcookies = $.cookie('csrftoken');
    var self_id = self.parentElement.parentElement.children[0].value;
    swal({
        title: "您确定删除吗?",
        text: "数据删除后 , 您将无法恢复 !",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    }).then((willDelete) => {
        if (willDelete) {
            $.ajax({
                type: "post",
                url: "/manageradmin/tjd_del/",
                headers: {'X-CSRFtoken': csrfcookies},
                data: {
                    "id": self_id,
                },
                success: function (data, status) {
                    if (status == 'success') {
                        swal("噗 , 删除成功 ! ", {
                            icon: "success",
                        }).then(
                            (success_confirm) => {
                                location.reload();
                            }
                        );
                    }
                }
                ,
            });
        } else {
            swal("已经取消删除啦 ! ");
        }
    });

}

function modify_msg(self, per_id) {
    // change_msg
    person = {
        'name': self.parentElement.children[1].innerText,
        'work_number': self.parentElement.children[2].innerText,
        'skills': self.parentElement.children[3].innerText,
        'future_direction': self.parentElement.children[5].innerText,
        'location': self.parentElement.children[6].innerText,
        'level': self.parentElement.children[7].innerText,
    };
    modify = document.getElementById('formemodal').children[0].lastElementChild.lastElementChild.lastElementChild.children;
    modify[0].children[1].value = person['name'];
    modify[1].children[1].value = person['work_number'];
    modify[4].children[1].value = person['location'];
    modify[5].children[1].value = person['level'];

}