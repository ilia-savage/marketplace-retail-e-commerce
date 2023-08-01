<template lang="">
    <div>
        <div class="field is-6">
            <label class="label" for="name">Name</label>
            <div class="control" >
                <input class="input" type="text" placeholder="Text input" id="name" v-model="name">
            </div>
            <label class="label" for="lastname">Last name</label>
            <div class="control" >
                <input class="input" type="text" placeholder="Text input" id="lastname" v-model="last_name">
            </div>
            <div class="field">
                <label class="label" for="email">Email</label>
                <div class="control has-icons-left has-icons-right">
                    <input class="input" type="email" placeholder="Email input" id="email" v-model="email">
                    <span class="icon is-small is-left">
                    <i class="fas fa-envelope"></i>
                    </span>
                    <span class="icon is-small is-right">
                    <i class="fas fa-exclamation-triangle"></i>
                    </span>
                </div>
                </div>
                <label class="label" for="name">Password</label>
                <div class="control" >
                    <input class="input" type="password" placeholder="Text input" id="password" v-model="password">
                </div>
                <div class="field is-grouped">
                <div class="control">
                    <button class="button is-link" @click="register()">Submit</button>
                </div>
                <div class="control">
                    <button class="button is-link is-light">Cancel</button>
                </div>
            </div>
            
        </div>
    </div>
</template>
<script>
import axios from 'axios';

export default {
    data() {
        return {
            status: '',
            name: '',
            last_name: '',
            email: '',
            password: ''
        }
    },
    mounted() {
    },
    methods: {
        async register() {
            await axios
                .post('/api/v1/register/', {
                    "name": this.name,
                    "last_name": this.last_name,
                    "username": this.email,
                    "password": this.password
                }
                    
                )
                .then(response => {
                    console.log(response.data)
                    this.status = response.data.message
                })
                .catch(error => {
                    console.log(error)
                })
        }
    },
}
</script>
<style lang="">
    
</style>