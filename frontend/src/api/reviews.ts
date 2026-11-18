// Product reviews on the menu page, loaded from the pizzeria's own API.
import { config } from '../config'

export interface Review {
  id: number
  author: string
  rating: number
  text: string
}

export async function loadReviews (productId: number): Promise<Review[]> {
  const response = await fetch(
    `${config.apiBaseUrl}/rest/products/${productId}/reviews`,
    {
      method: 'GET',
      headers: {
        Accept: 'application/json',
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    }
  )
  if (!response.ok) {
    return []
  }
  const body = await response.json()
  return body.data as Review[]
}
