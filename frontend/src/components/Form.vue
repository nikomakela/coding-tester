<script lang="ts">
import { ref, onMounted, watch, toRefs, computed, defineComponent } from 'vue'
import { wait } from '../util'

export default defineComponent({
  setup() {
    const isSaving = ref(false)

    return {
      isSaving,
    }
  },
  methods: {
    async onSubmit(e: Event) {
      e.preventDefault()
      this.isSaving = true
      console.log('onSubmit', this.isSaving)
      await wait(1000)
      console.log('wait complete')
      this.isSaving = false
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

      <button type="submit" :class="{ saving: isSaving }" :disabled="isSaving">
        <span v-if="isSaving">Testing your solution... </span>
        <span v-else> Submit </span>
      </button>
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
.is-saving {
  @apply bg-gray-500 cursor-wait;
}
button:disabled {
}
</style>