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
              placeholder="Name"
              addon-left-icon="ni ni-hat-3"
              v-model="register.name"
            />

            <input
              class="form-control mb-3"
              placeholder="Email"
              addon-left-icon="ni ni-email-83"
              v-model="register.email"
              focused
            />

            <input
              class="form-control mb-3"
              placeholder="Password"
              type="password"
              addon-left-icon="ni ni-lock-circle-open"
              v-model="register.password"
            />

            <!-- <div class="text-muted font-italic">
              <small
                >password strength:
                <span class="text-success font-weight-700">strong</span></small
              >
            </div> -->

            <!-- <div class="row my-4">
              <div class="col-12">
                <base-checkbox class="custom-control-alternative">
                  <span class="text-muted"
                    >I agree with the <a href="#!">Privacy Policy</a></span
                  >
                </base-checkbox>
              </div>
            </div> -->
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
export default {
  name: "register",
  data() {
    return {
      register: {
        name: "",
        email: "",
        password: "",
      },
    };
  },
  methods:{
    newRegister(){
      console.log("name:"+this.register.name+ ", email:"+this.register.email+", password:"+ this.register.password);
      //comprobar que el email tiene formato email
      //comprobar que la contraseña contiene numeros, mayusculas, minusculas y mas de 6 caracteres
      //comprobar que no existe ya el usuario
      //si es asi todo se graba en base de datos
    }
  }
};
</script>
<style></style>
