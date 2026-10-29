export async function fetchRooms(team: string): Promise<string[]> {
  const response = await fetch(`/api/rooms/schedule?room=${encodeURIComponent(team)}`)
  return response.json()
}

export const getRooms = async (team: string) => {
  return fetchRooms(team)
}
