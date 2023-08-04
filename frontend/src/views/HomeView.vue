<template>
  <div class="hero-banner">
    <a href="#" class="hero-banner__link">
      <img src="@/assets/img/banner.jpg" alt="banner" class="hero-banner__image">
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
    <a href="#" class="category-card" v-for="category in categories" v-bind:key="category.id">
      
      <div class="category-card__image-wrapper">
        <img class="category-card__image" :src="category.image" alt="category">
      </div>
      <p class="category-card__title">{{ category.name }}</p>
      
    </a>
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
        <p class="product-card__specs">Lorem ipsum dolor sit amet cdddddddddddonsectetur adipisicing elit. Ullam nostrum itaque enim aliquid aut, nu. Ullam nostrum itaque enim aliquid aut, nulla placeat eligendi . Ullam nostrum itaque enim aliquid aut, nulla placeat eligendi . Ullam nostrum itaque enim aliquid aut, nulla placeat eligendi lla placeat eligendi culpa. Ducimus, officiis.</p>
        <div class="product-card__wrapper">
          <div class="product-card__price-wrapper">
            <p class="product-card__price-old">$19999</p>
            <p class="product-card__price">${{ product.price }}</p>
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
  data() {
    return {
      latestProducts: [],
      categories: []
    }
  },
  components: {

  },
  mounted() {
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


</style>
