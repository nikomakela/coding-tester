<script lang="ts">
import { ref, defineComponent, Ref } from 'vue'
import { checkImplementation } from '../api'

enum FormStatus {
  Initial = 'initial',
  Success = 'success',
  Error = 'error',
}

export default defineComponent({
  setup() {
    const isSaving = ref(false)
    const formStatus: Ref<FormStatus> = ref(FormStatus.Initial)
    const formData = ref({
      implementationEndpoint: 'https://fibonacci-sequence-test.herokuapp.com/',
      id: null,
      applicant_address: null,
      source_code_url: null,
      format: 'json',
    })

    return {
      isSaving,
      formStatus,
      formData,
    }
  },
  methods: {
    async checkSolution(e: Event) {
      e.preventDefault()
      this.isSaving = true
      console.log('onSubmit', this.formData.implementationEndpoint)
      // await wait(1000)
      // console.log('wait complete')
      const json = await checkImplementation(
        'fibonacci',
        this.formData.implementationEndpoint
      )
      console.log(json)
      this.isSaving = false
      if (json.results?.id) {
        this.formStatus = FormStatus.Success
      }
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

    <form>
      <div class="form-group">
        <label for="">URL address of the endpoint of your implementation</label>
        <input
          type="text"
          v-model="formData.implementationEndpoint"
          placeholde="Endpoint URL..."
        />
      </div>

      <div v-if="formStatus === 'initial'">
        <button
          @click="checkSolution"
          :class="{ saving: isSaving }"
          :disabled="isSaving"
        >
          <span v-if="isSaving">Testing your solution... </span>
          <span v-else> Submit </span>
        </button>
      </div>

      <div v-if="formStatus === 'success'">
        <h2>Congrats! The tests were correct!</h2>
      </div>
    </form>
  </div>
</template> 

<style scoped>
.form-group {
  @apply flex flex-col mb-4 text-black;
}
form {
  @apply mb-8;
}
label {
  @apply text-white;
}
input {
  @apply p-2;
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