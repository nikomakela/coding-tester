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
  const params = {
    format: 'json',
    endpoint_url: implementationEndpointUrl,
  }
  const formParams = new URLSearchParams(params)

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

export default {
  getInstructions,
}
