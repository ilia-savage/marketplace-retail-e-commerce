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
                  <form action="/search" methods="get" >
                    <input type="text" id="search" placeholder="Поиск" name="query" required>
                    
                    <button class="navbar__search-button" type="submit">
                        <img src="@/assets/img/magnifier.svg" alt="search-icon" class="navbar__search-icon" height="26">
                    </button>
                  </form>
                </div>
            </div>
            <div class="navbar__end-wrapper icons">
                <router-link to="/login" class="icons__wrapper icon" v-if="user == ''" :key="loginKey">
                    <img src="@/assets/img/login.svg" alt="login" class="icon__image">
                    <p class="icon__title">Войти</p>
                </router-link>
                <router-link to="/profile" class="icons__wrapper icon" v-else>
                    <img src="@/assets/img/login.svg" alt="login" class="icon__image">
                    <p class="icon__title">{{ user.name }}</p>
                </router-link>
                <router-link to="/cart" class="icons__wrapper icon">
                    <img src="@/assets/img/cart.svg" alt="cart" class="icon__image">
                    {{ cartTotalLength }}
                    <p class="icon__title">Корзина</p>
                </router-link>
                
            </div>
        </nav>
      </div>
    </header>

    <div class="is-loading-bar has-text-centered" :class="{'is-loading': $store.state.isLoading}">
      <div class="lds-dual-ring"></div>
    </div>
    <main class="main">
      <div class="_container">
        <router-view v-if="user" v-on:detail="detail" v-on:detail-login="detailLogin" v-on:check-login="checkLogin" v-on:check-login-profile="checkLoginProfile"/>

        <router-view v-else v-on:detail="detail" v-on:detail-login="detailLogin" v-on:check-login="checkLogin" v-on:check-login-profile="checkLoginProfile"/>

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
      anonymous: true,
      loginKey: 0,
      cart: {
        items: []
      }
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
  },
  created() {
    this.detail();
  },
  mounted() {
      this.cart = this.$store.state.cart
    },
  methods: {
    checkLogin() {
      console.log(this.user)
      if (this.user != '') {
          this.$router.push('/')
      }
    },
    checkLoginProfile() {
      console.log(this.user)
      if (this.user == '') {
          this.$router.push('/')
      }
    },
    async detailLogin() {
      await axios
      .get(`/api/v1/`,
      {
          withCredentials: true,
      }
      )
      .then(response => {
          this.user = response.data
          this.anonymous = false
          this.forceRerender()
          console.log(response.data)
          console.log("im here")
      })
      .catch(error => {
          console.log(error)
      })

      this.$router.push('/profile')
    },
    async detail() {
      await axios
      .get(`/api/v1/`,
      {
          withCredentials: true,
      }
      )
      .then(response => {
          this.user = response.data
          this.anonymous = false
          this.forceRerender()
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
      width: 95%;
      position: relative;
    }
    &__logo {
        width: 350px;
        justify-self: flex-start;
    }
    &__search-button { 
        position: absolute;
        // right: 45px;
        // top: 15px;
        display: inline;

        height: 50px;

        width: 50px; 
        top: 4px;
        right: 10px;

        border-radius: 50%;
        outline: none;
        border: transparent;
        cursor: pointer;


        &:hover {
          box-shadow: 0 0.5em 1em -0.125em rgba(10, 10, 10, 0.3);

          background-color: white;
        }

    }
    &__search-icon {
        height: 26px;
        display: inline;
        position: absolute;
        right: 12px;
        bottom: 12px;
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
.product-card{
  background-color: white;
  height: 320px;
  min-width: 230px;
  border-radius: 6px;
  border: 2px solid #eeeeee;

  box-shadow: 0 0.5em 1em -0.125em rgba(10, 10, 10, 0.1);
  
  max-width: 256px;
  max-height: 350px;

  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 5;
  overflow: hidden;
  color: #151528;

    // margin: 0 30px;
    &__wrapper {
        display: flex;
    }
    &__link {
      display: block;
      padding: 20px;
      text-decoration: none;

      &:focus{
        color: #151528;
      }
    }
    &__title {
        font-size: 20px;
        font-weight: 700;
        // text-align: center;
        margin-top: 20px;
        margin-bottom: 10px;
        color: #151528;

        &:hover {
          color: #ff9100;
        }
    }
    
    &__buy-image {
        width: 140px;
    }
    &__specs {
        margin: 10px 0;
        height: 30px;
        overflow: hidden;
        max-width: 100%;
        text-overflow: ellipsis;
        width: fit-content;
        white-space: nowrap;
        word-wrap: break-word;
        color: #151528;

    }
    &__price-old {
        text-decoration:line-through;
        font-size: 16px;
        color: #151528;
        // letter-spacing: 1px;
    }
    &__image-container {
      display: flex;
      height: 140px;
      width: 190px;
      justify-content: center;
      margin: 0 auto;

    }
    &__image {
      object-fit: contain;
      max-height: 140px;
      max-width: 190px;
      margin: 0 auto;
    }
    &__price {
        font-size: 20px;
        font-weight: 700;
        color: #151528;

        // letter-spacing: 1px;
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
