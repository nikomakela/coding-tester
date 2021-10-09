<script lang="ts">
import { defineComponent } from 'vue'
import { Input } from './form'
export default defineComponent({
  setup() {},
  methods: {
    onSubmit(e) {
      e.preventDefault()
      console.log('onSubmit')
    },
  },
})
</script>

<template>
  <div class="text-white">
    <h2 class="text-2xl mb-4">Test your solution</h2>

    <p class="mb-2">
      With this tool, you can run automated tests against your implementation.
    </p>

    <form @submit="onSubmit">
      <div class="form-group">
        <label for="">URL address of the endpoint of your implementation</label>
        <input type="text" />
      </div>

      <button type="submit">Submit</button>
    </form>
  </div>
</template> 

<style scoped>
.form-group {
  @apply flex flex-col mb-4;
}
form {
  max-width: 500px;
}
label {
  @apply text-white;
}
button {
  @apply bg-blue-500 px-4 py-2;
}
</style>