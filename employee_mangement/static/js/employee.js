async function loadEmployees(){

    const response =
    await fetch("/employees");

    const employees =
    await response.json();

    let rows = "";

    employees.forEach(emp => {

        rows += `
        <tr>

            <td>${emp.employee_id}</td>

            <td>
            ${emp.first_name}
            </td>

            <td>
            ${emp.email}
            </td>

        </tr>
        `;
    });

    const table =
    document.getElementById(
        "employeeTable"
    );

    if(table){

        table.innerHTML = rows;
    }
}

async function saveEmployee(){

    await fetch(
        "/employees",
        {

            method: "POST",

            headers:{
                "Content-Type":
                "application/json"
            },

            body: JSON.stringify({

                first_name:
                document.getElementById(
                "first_name").value,

                last_name:
                document.getElementById(
                "last_name").value,

                email:
                document.getElementById(
                "email").value,

                phone:
                document.getElementById(
                "phone").value,

                gender:"Male",

                age:
                parseInt(
                document.getElementById(
                "age").value),

                designation:
                document.getElementById(
                "designation").value,

                joining_date:
                document.getElementById(
                "joining_date").value,

                salary:
                parseFloat(
                document.getElementById(
                "salary").value),

                department_id:
                parseInt(
                document.getElementById(
                "department_id").value)
            })
        }
    );

    alert(
        "Employee Saved Successfully"
    );
}

loadEmployees();