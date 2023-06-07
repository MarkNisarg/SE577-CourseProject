export interface RepositoryApiInterface {
  description: string,
  name: string,
  open_issues: number,
  private: boolean,
  html_url: string
}

export interface PullRequestsApiInterface {
  base: {
    ref: string
  }
  head: {
    ref: string,
    repo: {
      name: string
    }
  },
  html_url: string,
  id: number,
  number: number,
  state: string,
  title: string,
  user: {
    login: string
  }
}

export interface PullRequestCommentsApiInterface {
  body: string
}

export interface ApiErrorInterface {
  isError: boolean,
  errorCode: number,
  errorMessage: string
}
