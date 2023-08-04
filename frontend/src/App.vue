<template>
  <div class="app-container">
    <header class="header">
      <div class="_container">
        <nav class="navbar">
            <router-link to="/">
              <img src="@/assets/img/logo.svg" alt="logo" class="navbar__logo">
            </router-link>
            <div class="navbar__middle-wrapper">
                <div class="navbar__links-wrapper">
                    <a href="#" class="navbar__link">Акции</a>
                    <a href="#" class="navbar__link">Новости</a>
                    <a href="#" class="navbar__link">Доставка</a>
                    <a href="#" class="navbar__link">О магазине</a>
                    <a href="#" class="navbar__link">Контакты</a>
                </div>
                <div class="navbar__search-bar">
                    <input type="text" id="search" placeholder="Поиск">
                    <label for="search" class="navbar__search-label">
                        <img src="@/assets/img/magnifier.svg" alt="search-icon" class="navbar__search-icon" height="26">
                    </label>
                </div>
            </div>
            <div class="navbar__end-wrapper icons">
                <a href="#" class="icons__wrapper icon">
                    <img src="@/assets/img/login.svg" alt="login" class="icon__image">
                    <p class="icon__title">Войти</p>
                </a>
                <a href="#" class="icons__wrapper icon">
                    <img src="@/assets/img/cart.svg" alt="cart" class="icon__image">
                    <p class="icon__title">Корзина</p>
                </a>
                
            </div>
        </nav>
      </div>
    </header>

    <div class="is-loading-bar has-text-centered" :class="{'is-loading': $store.state.isLoading}">
      <div class="lds-dual-ring"></div>
    </div>
    <main class="main">
      <div class="_container">
        <router-view/>
      </div>
    </main>

    <footer class="footer">
      <div class="_container">
        <p class="has-text-centered"> Copyright (c) 2023</p>
      </div>
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
// @import '../node_modules/bulma';
@import url('./assets/css/reset.css');

@import url('https://fonts.googleapis.com/css2?family=PT+Sans:wght@400;700&display=swap');
html, body {
    // max-width: 1440px;
    margin: 0 auto;
    height: 100%;
    font-family: 'PT Sans', sans-serif;
    letter-spacing: 0.03rem;
}

html > body {
  background-color: rgb(248, 248, 248);
}

// body{
//     // padding: 0 25px;
//     // margin-top: 35px;
    
// }
._container {
  padding: 0 25px;
  max-width: 1440px;
  margin: 0 auto;
}
header {
  background-color: white;
  border-bottom: 1px solid #d7d4d4;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 1px;

}
.navbar {
    padding-top: 50px;
    padding-bottom: 20px;
    display: flex;
    justify-content: space-between;
    
    &__search-bar {
      width: 90%;
    }
    &__logo {
        width: 350px;
        justify-self: flex-start;
    }
    &__search-label { 
        position: relative;
        right: 45px;
        top: 15px;
    }
    &__search-icon {
        height: 26px;
        display: inline-block;
        position: absolute;
    }
    &__middle-wrapper{
        width: 100%;
        margin-left: 30px;

        #search {
            background-color: #efeff2;
            font-size: 16px;
            border: white;
            outline: none;
            width: 100%;
            height: 58px;
            position: relative;
            border-radius: 10px;
            padding-left: 20px;
            transition: all 0.3s;

            &:hover{
                background-color: white;
                border: 1px solid #d7d4d4;

                // border: 2px solid rgb(189, 189, 189);
                box-shadow: rgba(0, 0, 0, 0.2) 0px 5px 15px;
            }
            &:focus{
                background-color: white;
                border: 1px solid #d7d4d4;

                // border: 2px solid rgb(189, 189, 189);
                box-shadow: rgba(0, 0, 0, 0.2) 0px 5px 15px;
            }
        }
    }
    &__links-wrapper{
        position: relative;
        bottom: 10px;
    }
    &__link{
        font-size: 16px;
        margin: 0 8px;
        color: #151528;
        text-decoration: none;

        &:hover{
            color: #ff9100;
            transition: all 0.3s;
        }
    }
    .icons {
        display: flex;
        margin-right: 80px;
        .icon {
            margin: 0 10px;
            position: relative;
            top: 15px;
            text-decoration: none;
            color: #151528;
            &:hover{
                color: rgb(74, 74, 74)
            }
            &:active{
                color: #ff9100;
            }
            
            &__image {
                height: 50px;
                
            }
        }
    }
}

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
