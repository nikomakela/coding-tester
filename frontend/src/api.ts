export interface FormData {
  implementationEndpoint: string
  id: string
  applicant_address: string
  source_code_url: string
  format: string
}

export const getInstructions = async () => {
  console.log('instruction', import.meta.env.VITE_API_ENDPOINT)
  const response = await fetch(
    `${import.meta.env.VITE_API_ENDPOINT}/fibonacci/solve?format=json`
  )
  const json = await response.json()
  return json
}

export const checkImplementation = async (
  testType: string,
  implementationEndpointUrl: string
) => {
  const formParams = new URLSearchParams({
    format: 'json',
    endpoint_url: implementationEndpointUrl,
  })

  const response = await fetch(
    `${import.meta.env.VITE_API_ENDPOINT}/${testType}/check`,
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: formParams,
    }
  )
  const json = await response.json()
  console.log(json)
  return json
}

export const submitInformation = async (testType: string, formData: any) => {
  const formParams = new URLSearchParams(formData)

  const response = await fetch(
    `${import.meta.env.VITE_API_ENDPOINT}/${testType}/submit/${formData.id}`,
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: formParams,
    }
  )
  const json = await response.json()
  console.log(json)
  return json
}

export default {
  getInstructions,
}
