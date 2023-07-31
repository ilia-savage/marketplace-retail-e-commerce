<template>
  <div class="home">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">
          Latest
        </h2>
      </div>
      <div class="column product is-2" v-for="product in latestProducts" v-bind:key="product.id">
        <div class="box">
          <figure class="image mb-4">
            <img :src="product.get_thumbnail" class="image__img" alt="thumbnail">
          </figure>

          <h3 class="is-size-4">{{ product.name }}</h3>
          <p class="is-size-6 has-text-grey">${{ product.price }}</p>

          <router-link :to="'/product/' + product.id">View</router-link>
        </div>
      </div>
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
      latestProducts: []
    }
  },
  components: {
    
  },
  mounted() {
    this.getLatestProducts()
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
    }
  }
}
</script>

<style>
.image{
  /* margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem; */
  object-fit: fill;
  /* max-height: 115px; */
  max-width: 150px;
  max-height: 180px;
}

/* .image__img {
  object-fit: contain;
  max-height: 115px;
  min-height: 135px;
  max-height: 140;
} */

.product{
  max-width: 250px;
  min-width: 250px;
  max-height: 300px;
}

</style>
