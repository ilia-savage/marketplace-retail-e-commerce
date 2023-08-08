<template lang="">
    <div>
        <div class="field is-6">
            
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
                <div class="notification is-danger" v-show="error">
                    Incorrect email or password
                </div>
                <div class="field is-grouped">
                <div class="control">
                    <button class="button is-link" @click="login()">Submit</button>
                </div>
                <router-link to='/register/'>Sign Up</router-link>
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
            password: '',
            error: false,
        }
    },
    mounted() {
    },
    methods: {
        async login() {
            await axios
                .post('/api/v1/login/', {
                    "username": this.email,
                    "password": this.password
                },
                {
                    withCredentials: true
                }
                    
                )
                .then(response => {
                    console.log(response.data)
                    this.status = response.data.message
                })
                .catch(error => {
                    console.log(error)
                    console.log(this.email)
                    console.log(this.password)
                    this.error = true
                })
        }
    },
}
</script>
<style lang="">
    
</style>