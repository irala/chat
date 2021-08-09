<template>
  <div class="row justify-content-center">
    <div class="col-lg-5 col-md-7">
      <div class="card bg-secondary shadow border-0">
        <div class="card-body px-lg-5 py-lg-5">
          <div class="text-center text-muted mb-4">
            <small>Sign in with credentials</small>
          </div>
          <!-- <form role="form"> -->
            <input
              class="form-control mb-3"
              placeholder="Username"
              addon-left-icon="ni ni-email-83"
              v-model="login.username"
            />

            <input
              class="form-control mb-3"
              placeholder="Password"
              type="password"
              addon-left-icon="ni ni-lock-circle-open"
              v-model="login.password"
            />
            <div role="alert" class="alert alert-warning" v-show="isIncorrect">
              <strong>Warning!</strong> Username o password incorrect!
            </div>
            <div class="text-center" @click="validateLogin">
              <base-button type="primary" class="my-4" 
                >Sign in</base-button
              >
            </div>
          <!-- </form> -->
        </div>
      </div>
      <div class="row mt-3">
        <div class="col-6">
          <!-- <a href="#" class="text-light"><small>Forgot password?</small></a> -->
        </div>
        <div class="col-6 text-right">
          <router-link to="/register" class="text-light"
            ><small>Create new account</small></router-link
          >
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "login",
  data() {
    return {
      isIncorrect: false,
      login: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    validateLogin() {
      console.log("entro a login");

      //comprobar que existe ya el usuario
      const path = "/identity/login";
      console.log(path);
      axios
        .post(path, {
          username: this.login.username,
          password: this.login.password,
        })
        .then((res) => {
          let result = res;
          console.log(result.data);
          console.log("login");
          //redirigir a app
          let to = { name: "dashboard" };
          this.$router.push(to);
        })
        .catch((error) => {
          this.isIncorrect = true;
          console.error(error);
          console.log("incorrect" + this.isIncorrect);
        });
    },
  },
};
</script>
<style></style>
