<script lang="ts">
import { ref, defineComponent, Ref } from 'vue'
import { checkImplementation, submitInformation } from '../api'

enum FormStatus {
  Initial = 'initial',
  Success = 'success',
  Error = 'error',
  Final = 'final',
}

interface FormData {
  endpoint_url: string | null
  id: string | null
  applicant_address: string | null
  source_code_url: string | null
  format: string
}

export default defineComponent({
  setup() {
    const isSaving = ref(false)
    const formStatus: Ref<FormStatus> = ref(FormStatus.Initial)
    const formData: Ref<FormData> = ref({
      endpoint_url: 'https://fibonacci-sequence-test.herokuapp.com/',
      id: null,
      applicant_address: 'jussi.polkki@mavericks.fi',
      source_code_url: 'https://github.com/nikomakela/coding-tester',
      format: 'json',
    })

    return {
      isSaving,
      formStatus,
      formData,
    }
  },
  methods: {
    async checkSolution() {
      if (!this.formData.endpoint_url) return

      this.isSaving = true
      const json = await checkImplementation(
        'fibonacci',
        this.formData.endpoint_url
      )
      console.log(json)
      this.isSaving = false
      if (json.results?.id) {
        this.formData.id = json.results.id
        this.formStatus = FormStatus.Success
      }
    },
    async finalSubmit() {
      this.isSaving = true
      console.log('finalSubmit')
      const json = await submitInformation('fibonacci', this.formData)
      console.log(json)
      this.isSaving = false
      this.formStatus = FormStatus.Final
    },
  },
})
</script>

<template>
  <div class="text-white">
    <h2 class="text-2xl mb-4">Test your solution</h2>

    <p>
      With this tool, you can run automated tests against your implementation.
    </p>

    <form class="mt-8">
      <div class="form-group">
        <label for=""
          >URL address of the endpoint of your implementation:</label
        >
        <input
          type="text"
          v-model="formData.endpoint_url"
          placeholder="Endpoint URL..."
          :disabled="formStatus === 'success'"
        />
      </div>

      <div v-if="formStatus === 'initial'">
        <button
          @click="checkSolution"
          :class="{ 'is-saving': isSaving }"
          :disabled="isSaving"
        >
          <span v-if="isSaving">Testing your solution... </span>
          <span v-else> Submit </span>
        </button>
      </div>

      <div v-if="formStatus === 'success'">
        <h2 class="px-8 py-4 my-8 bg-green-500">
          Congratulations! Your implementation passed all tests!
        </h2>

        <p>Now fill the rest of the fields and we'll be in touch with you!</p>

        <div class="form-group">
          <label for="email">Your email:</label>
          <input
            id="email"
            type="email"
            v-model="formData.applicant_address"
            placeholde="Input email"
          />
        </div>

        <div class="form-group">
          <label for="source_code"
            >Public URL to the repository where your source code is located at
            (eg. Github, Bitbucket):</label
          >
          <input
            id="source_code"
            type="email"
            v-model="formData.source_code_url"
            placeholde="Input URL"
          />
        </div>

        <div v-if="formStatus === 'success'">
          <button
            @click="finalSubmit"
            :class="{ 'is-saving': isSaving }"
            :disabled="isSaving"
          >
            <span v-if="isSaving">Submitting your information... </span>
            <span v-else> Submit </span>
          </button>
        </div>
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
  @apply text-white mb-2;
}
input {
  @apply p-2;
}
input:disabled {
  @apply cursor-not-allowed;
}
button {
  @apply bg-blue-500 px-4 py-2;
}
.is-saving {
  @apply bg-gray-500 cursor-wait;
}
button:disabled {
}

h2 {
  @apply mb-4;
}
p {
  @apply mb-2;
}
</style>