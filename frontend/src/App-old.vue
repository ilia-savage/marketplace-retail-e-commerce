<template>
  <div class="app-container">
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
        <div class="navbar-start">
          <div class="navbar-item">
            <form action="/search" methods="get">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" placeholder="Search" class="input" name="query">
                </div>

                <div class="control">
                  <button class="button is-success">
                    <span class="icon">
                      <i class="fas fa-search"></i>
                    </span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
        <div class="navbar-end">
          <router-link to="/smth" class="navbar-item">smth</router-link>
          <router-link to="/smth" class="navbar-item">smth</router-link>
          
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/login" class="button is-light" :key="loginKey" v-if="user">{{ user.username }}</router-link>
              <router-link to="/login" class="button is-light" v-else>Log in</router-link>
              <router-link to="/cart" class="button is-success">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Cart {{ cartTotalLength }}</span>
              </router-link>

            </div>
          </div>
        </div>
      </div>
    </nav>

    <div class="is-loading-bar has-text-centered" :class="{'is-loading': $store.state.isLoading}">
      <div class="lds-dual-ring"></div>
    </div>
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
      cart: {
        items: []
      }
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
  },
  mounted() {
      this.detail()
      this.cart = this.$store.state.cart
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
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0

      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity
      }

      return totalLength
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';

.wrapper{
  max-width: 1500px;
  margin: 0 auto;
}
$container-max-width: 1500px;

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}
</style>
