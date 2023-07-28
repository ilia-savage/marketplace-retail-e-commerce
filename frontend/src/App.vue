<template>
  <div class="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item" @click="forceRerender()"><strong>ILTECH</strong></router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true">

          </span>
          <span aria-hidden="true">
            
          </span>
          <span aria-hidden="true">
            
          </span>
        </a>
      </div>
      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
        <div class="navbar-end">
          <router-link to="/smth" class="navbar-item">smth</router-link>
          <router-link to="/smth" class="navbar-item">smth</router-link>
          
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/login" class="button is-light" :key="loginKey" v-if="user">{{ user.username }}</router-link>
              <router-link to="/login" class="button is-light" v-else>Log in</router-link>
              <router-link to="/cart" class="button is-success">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Cart</span>
              </router-link>

            </div>
          </div>
        </div>
      </div>
    </nav>
    <section>
      <router-view/>
    </section>



    <footer class="footer">
      <p class="has-text-centered"> Copyright (c) 2023</p>
    </footer>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      showMobileMenu: false,
      user: '',
      loginKey: 0,
    }
    
  },
  mounted() {
      this.detail()
    },
  methods: {
    detail() {
      axios
      .get(`/api/v1/`,
      {
          withCredentials: true,
      }
      )
      .then(response => {
          
          this.user = response.data
          console.log(response.data)
      })
      .catch(error => {
          console.log(error)
      })
    },
    // force rerender login element
    forceRerender () {
      this.loginKey += 1
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';

.wrapper{
  max-width: 1200px;
  margin: 0 auto;
}
</style>
