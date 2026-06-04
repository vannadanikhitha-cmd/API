async function login() {

    const response = await fetch(
        "/auth/login",
        {
            method: "POST",

            headers: {
                "Content-Type":
                "application/json"
            },

            body: JSON.stringify({

                username:
                document.getElementById(
                    "username"
                ).value,

                password:
                document.getElementById(
                    "password"
                ).value
            })
        }
    );

    const data =
        await response.json();

    if(data.access_token){

        localStorage.setItem(
            "token",
            data.access_token
        );

        window.location.href =
        "/dashboard";
    }
}