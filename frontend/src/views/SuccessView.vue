<template lang="en">
    <div class="success-page-wrapper">
        <strong>Заказ принят в обработку</strong>
        <br>
        <router-link to="/profile"> Перейти к вашим заказам...</router-link>
    </div>
</template>
<script>
export default {
    
}
</script>
<style lang="scss">
    .success-page-wrapper {
    background-color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 0 auto;
    max-width: 400px;
    height: 200px;
    box-shadow: 0 0.5em 1em -0.125em rgba(10, 10, 10, 0.2);
    border-radius: 5px;
    padding: 30px;
    margin-top: 30px;
}
</style>