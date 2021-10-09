<script lang="ts">
import { ref, defineComponent, Ref } from 'vue'
import { checkImplementation, submitInformation } from '../api'
import { getAssignmentName } from '../util'

enum FormStatus {
  Initial = 'initial',
  Success = 'success',
  Error = 'error',
  Final = 'final',
}

interface FormData {
  endpoint_url: string | null
  id: string | null
  applicant_name: string | null
  applicant_address: string | null
  applicant_phone: string | null
  own_tech_competence: string
  work_experience: string
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
      applicant_name: 'Jussi Pölkki & Niko Kivelä',
      applicant_address: 'jussi+niko@mavericks.fi',
      applicant_phone: '+358501234567',
      source_code_url: 'https://github.com/nikomakela/coding-tester',
      own_tech_competence: 'Typescript & Django',
      work_experience: '99 years',
      format: 'json',
    })
    const formError: Ref<string | null> = ref(null)
    const testAssignment = getAssignmentName()

    return {
      isSaving,
      formStatus,
      formData,
      testAssignment,
      formError,
    }
  },
  methods: {
    async checkSolution() {
      if (!this.formData.endpoint_url) return

      this.isSaving = true
      this.formError = null

      const json = await checkImplementation(
        this.testAssignment,
        this.formData.endpoint_url
      )
      this.isSaving = false

      if (json.results?.id) {
        this.formData.id = json.results.id
        this.formStatus = FormStatus.Success
      } else {
        this.formError = `${json.reason}, ${json.problem}`
      }
    },
    async finalSubmit() {
      this.isSaving = true
      const json = await submitInformation(this.testAssignment, this.formData)
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
          :disabled="
            isSaving || formStatus === 'success' || formStatus === 'final'
          "
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

        <p v-if="formError" class="mt-4 bg-red-400 p-4">
          Error found in the solution: {{ formError }}
        </p>
      </div>

      <div v-if="formStatus === 'success' || formStatus === 'final'">
        <h2 class="px-8 py-4 my-8 bg-green-500">
          Congratulations! Your implementation passed all tests!
        </h2>

        <p>Now fill the rest of the fields and we'll be in touch with you!</p>

        <div class="form-group">
          <label for="email">Your name:</label>
          <input
            id="name"
            type="name"
            v-model="formData.applicant_name"
            placeholde="Input name"
            :disabled="isSaving || formStatus === 'final'"
          />
        </div>

        <div class="form-group">
          <label for="email">Your email:</label>
          <input
            id="email"
            type="email"
            v-model="formData.applicant_address"
            placeholde="Input email"
            :disabled="isSaving || formStatus === 'final'"
          />
        </div>

        <div class="form-group">
          <label for="email">Your phone number:</label>
          <input
            id="phone"
            type="phone"
            v-model="formData.applicant_phone"
            placeholde="Input phone"
            :disabled="isSaving || formStatus === 'final'"
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
            :disabled="isSaving || formStatus === 'final'"
          />
        </div>

        <div class="form-group">
          <label for="own_tech_competence"
            >Your favorite languages or tech:</label
          >
          <textarea
            id="own_tech_competence"
            type="email"
            v-model="formData.own_tech_competence"
            :disabled="isSaving || formStatus === 'final'"
          ></textarea>
        </div>

        <div class="form-group">
          <label for="work_experience">Your brief work experience:</label>
          <textarea
            id="work_experience"
            type="email"
            v-model="formData.work_experience"
            :disabled="isSaving || formStatus === 'final'"
          ></textarea>
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

        <div v-if="formStatus === 'final'">
          <h2 class="px-8 py-4 my-8 bg-green-500">
            Form submission was successful. Thank you for getting in touch.
            We'll get back to you as soon as possible.
          </h2>
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
textarea {
  @apply p-2 h-32;
}
input:disabled,
textarea:disabled {
  @apply cursor-not-allowed bg-gray-500;
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