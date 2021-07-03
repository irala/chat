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

            <div class="text-center">
              <base-button type="primary" class="my-4" @click="newRegister"
                >Create account</base-button
              >
            </div>
          </form>
        </div>
      </div>
      <div class="row mt-2">
        <!-- <div class="col-6">
          <a href="#" class="text-light">
            <small>Forgot password?</small>
          </a>
        </div> -->
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
      register: {
        username: "",
        password: "",
      },
    };
  },
  methods:{
    newRegister(){
      console.log("username:"+this.register.username+ ", password:"+ this.register.password);
      //comprobar que la contraseña contiene numeros, mayusculas, minusculas y mas de 6 caracteres
      //comprobar que no existe ya el usuario
      //si es asi todo se graba en base de datos
      const path = "/identity/register";
      console.log(path);
      axios
        .post(path,{username:this.register.username, password:this.register.password})
        .then((res) => {
          let result=res;
          console.log(result.data);
          console.log("dentro")
          //redirigir a app
            let to = { name: "dashboard" };
          this.$router.push(to);

        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  
  }
};
</script>
<style></style>
