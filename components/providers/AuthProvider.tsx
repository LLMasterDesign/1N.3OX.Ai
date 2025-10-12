'use client'

import { createContext, useContext, useEffect, useState } from 'react'

interface User {
  id: string
  email: string
  name: string
  subscriptionTier: 'free' | 'professional' | 'business' | 'enterprise'
}

interface AuthContextType {
  user: User | null
  loading: boolean
  login: (email: string, password: string) => Promise<void>
  logout: () => void
  signup: (email: string, password: string, name: string) => Promise<void>
}

const AuthContext = createContext<AuthContextType | undefined>(undefined)

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Check for existing session
    const checkAuth = async () => {
      try {
        const token = localStorage.getItem('auth_token')
        if (token) {
          // In a real app, you'd validate the token with your backend
          // For now, we'll just check if it exists
          const userData = localStorage.getItem('user_data')
          if (userData) {
            setUser(JSON.parse(userData))
          }
        }
      } catch (error) {
        console.error('Auth check failed:', error)
      } finally {
        setLoading(false)
      }
    }

    checkAuth()
  }, [])

  const login = async (email: string, password: string) => {
    try {
      // In a real app, you'd make an API call to your backend
      // For now, we'll simulate a login
      const mockUser: User = {
        id: '1',
        email,
        name: email.split('@')[0],
        subscriptionTier: 'free'
      }
      
      localStorage.setItem('auth_token', 'mock_token')
      localStorage.setItem('user_data', JSON.stringify(mockUser))
      setUser(mockUser)
    } catch (error) {
      throw new Error('Login failed')
    }
  }

  const signup = async (email: string, password: string, name: string) => {
    try {
      // In a real app, you'd make an API call to your backend
      // For now, we'll simulate a signup
      const mockUser: User = {
        id: '1',
        email,
        name,
        subscriptionTier: 'free'
      }
      
      localStorage.setItem('auth_token', 'mock_token')
      localStorage.setItem('user_data', JSON.stringify(mockUser))
      setUser(mockUser)
    } catch (error) {
      throw new Error('Signup failed')
    }
  }

  const logout = () => {
    localStorage.removeItem('auth_token')
    localStorage.removeItem('user_data')
    setUser(null)
  }

  return (
    <AuthContext.Provider value={{ user, loading, login, logout, signup }}>
      {children}
    </AuthContext.Provider>
  )
}

export function useAuth() {
  const context = useContext(AuthContext)
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider')
  }
  return context
}