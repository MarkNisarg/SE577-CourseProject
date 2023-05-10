export interface RepositoryApiInterface {
  contributors: string,
  description: string,
  languages: string,
  name: string,
  url: string
}

export interface ApiErrorInterface {
  isError: boolean,
  errorCode: number,
  errorMessage: string
}
