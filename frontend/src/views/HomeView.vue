<template>
  <div class="hero-banner">
    <a href="/product/24" class="hero-banner__link">
      <img src="@/assets/img/ad.png" alt="banner" class="hero-banner__image">
    </a>
  </div>
  <div class="popular-category-wrapper category">
    <h1 class="category__title">
      Популярные категории
    </h1>
    <a href="#" class="category__all-link">
      Все категории..
    </a>
  </div>
  <div class="category-card-wrapper">
    <router-link :to="'/category/' + category.id " class="category-card" v-for="category in categories" v-bind:key="category.id">
      
      <div class="category-card__image-wrapper">
        <img class="category-card__image" :src="category.image" alt="category">
      </div>
      <p class="category-card__title">{{ category.name }}</p>
      
    </router-link>
  </div>

  <div class="popular-category-wrapper category">
    <h3 class="category__title">
      Хиты продаж
    </h3>
  </div>
  <div class="hits-wrapper">
    <div class="product-card" v-for="product in latestProducts" v-bind:key="product.id">
      <router-link class="product-card__link" :to="'/product/' + product.id">
        <div class="product-card__image-container">
          <img class="product-card__image" :src="product.get_thumbnail" alt="product">
        </div>
        <p class="product-card__title">
          {{ product.name }}
        </p>
        <p class="product-card__specs"><span v-for="(value, key, index) in product.specs" :key="index">{{  value  }}, </span></p>
        <div class="product-card__wrapper">
          <div class="product-card__price-wrapper">
            <p class="product-card__price-old">{{ product.price }}</p>
            <p class="product-card__price">${{ product.final_price }} </p>
          </div>
          <div class="product-card__button-wrapper">
            <a class="product-card__buy-button" href="#">
              <img class="product-card__buy-image" src="@/assets/img/buy-button.svg" alt="buy-button">
            </a>
          </div>
        </div>
      </router-link>
    </div>
    
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';

export default {
  name: 'HomeView',
  // props: ['user'],

  data() {
    return {
      latestProducts: [],
      categories: [],
      ad: {},
    }
  },
  components: {

  },
  mounted() {
    // this.getAd()
    this.getLatestProducts();
    this.getCategories();
  },
  methods: {
    getLatestProducts() {
      axios
        .get('/api/v1/product/')
        .then(response => {
          this.latestProducts = response.data.results
        })
        .catch(error => {
          console.log(error)
        })
    },
    // async getAd() {
    //   await axios
    //     .get('http://127.0.0.1:8000/api/v1/ad/')
    //     .then(response => {
    //       console.log(response)
    //     })
    //     .catch(error => {
    //       console.log(error)
    //     })
    // },
    async getCategories() {
      await axios
        .get('/api/v1/category/')
        .then(response => {
          this.categories = response.data.results
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  
}
</script>

<style lang="scss">
main {
    .hero-banner {
        display: flex;
        justify-content: center;
        margin-top: 50px;

        &__image {
            height: auto; 
            max-height: 260px;
            max-width: 100%;
            object-fit: fill;
        }
    }
    .category{
        margin-top: 50px;

        &__title{
            font-size: 24px;
            font-weight: 700;
            line-height: 35px;
            font-style: bold;
        }
        &__all-link {
            font-size: 16px;
            color: #0038ff;
            margin-left: 10px;
        }
    }
    .category-card-wrapper {
        display: flex;
        flex-wrap: wrap;
        // flex-direction: row;
        margin-top: 20px;

        @media(max-width: 815px) {
          justify-content: center;
        }

        .category-card {
          background-color: white;
          margin: 5px;
          padding: 20px;
          max-width: 265px;
          max-height: 220px;
          border: 2px solid #eeeeee;
          border-radius: 10px;
          text-decoration: none;
          transition: all 0.2s;
          box-shadow: rgba(0, 0, 0, 0.05) 0px 5px 15px;


            &__image-wrapper {
              display: flex;
              justify-content: center;
            }
            &:hover{
                background-color: white;
                border: 2px solid #d7d4d4;

                // border: 2px solid rgb(189, 189, 189);
                box-shadow: rgba(0, 0, 0, 0.3) 0px 5px 15px;
                
            }
            
            &__image {
              width: 220px;
              max-height: 140px;
              height: 140px;
              object-fit: contain;
            }

            &__title {
                font-size: 20px;
                text-align: center;
                color: #151528;
                
            }
        }
    }
    .hits-wrapper {
        display: flex;
        flex-wrap: wrap;
        gap: 22px;
        margin-top: 30px;
        
        @media(max-width: 815px) {
          justify-content: center;
        }
    }
}

.image {
  /* margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem; */
  object-fit: contain;
  /* max-height: 115px; */
  /* max-width: 150px; */
  height: 150px;
}

.products-wrapper {
  margin: 0 auto;
  max-width: 1500px;
}

.image__img {
  object-fit: contain;
  max-height: 140px;
}

.product {
  height: 350px;
  min-width: 230px;
  margin: 12px 12px;
  padding-left: 0px;
  padding-right: 0px;
}

.box {
  height: 350px;
  min-width: 230px;
}
.product-card__image-container {
  width: 215px;
}

</style>
