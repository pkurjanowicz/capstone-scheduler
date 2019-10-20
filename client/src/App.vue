<template>
  <div id="app">
    <Signin/>
    <Signup/>
  </div>
</template>

<script>
import Signin from './components/Signin.vue'
import Signup from './components/Signup.vue'

export default {
  name: 'app',
  components: {
    Signin,
    Signup
  }
}
</script>

<style>

</style>
