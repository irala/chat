<template>
  <div class="row justify-content-center">
    <div class="col-lg-5 col-md-7">
      <div class="card bg-secondary shadow border-0">
        <div class="card-body px-lg-5 py-lg-5">
          <div class="text-center text-muted mb-4">
            <small>Sign up with credentials</small>
          </div>
          <form role="form">
            <input
              class="form-control mb-3"
              placeholder="Username"
              addon-left-icon="ni ni-hat-3"
              v-model="register.username"
            />

            <input
              class="form-control mb-3"
              placeholder="Password"
              type="password"
              addon-left-icon="ni ni-lock-circle-open"
              v-model="register.password"
            />
            <div role="alert" class="alert alert-warning" v-show="notRegister">
              <strong>Warning!</strong> Username register!
            </div>
            <div class="text-center" @click="newRegister">
              <base-button type="primary" class="my-4" 
                >Create account</base-button
              >
            </div>
          </form>
        </div>
      </div>
      <div class="row mt-2">    
        <div class="col-6 text-right">
          <router-link to="/login" class="text-light">
            <small>Login into your account</small>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "register",
  data() {
    return {
      notRegister:false,
      register: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    newRegister() {
      console.log("entro a registrar")
      const path = "/identity/register";
      axios
        .post(path, {
          username: this.register.username,
          password: this.register.password,
        })
        .then((res) => {
          console.log("registrado")
          let result = res;
          console.log(result.data);
          let to = { name: "login" };
          this.$router.push(to);
        })
        .catch((error) => {
          console.error(error);
          this.notRegister = true
        });
    },
  },
};
</script>
<style></style>
