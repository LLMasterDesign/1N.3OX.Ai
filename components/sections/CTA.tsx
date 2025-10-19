import Link from 'next/link'
import { Button } from '@/components/ui/Button'
import { ArrowRightIcon } from '@heroicons/react/24/outline'

export function CTA() {
  return (
    <div className="bg-primary-600">
      <div className="px-6 py-24 sm:px-6 sm:py-32 lg:px-8">
        <div className="mx-auto max-w-2xl text-center">
          <h2 className="text-3xl font-bold tracking-tight text-white sm:text-4xl">
            Ready to optimize your AI prompts?
          </h2>
          <p className="mx-auto mt-6 max-w-xl text-lg leading-8 text-primary-100">
            Join thousands of users who are already getting better results with our 
            research-backed prompt optimization platform. Start your free trial today.
          </p>
          <div className="mt-10 flex items-center justify-center gap-x-6">
            <Link href="/signup">
              <Button size="lg" className="bg-white text-primary-600 hover:bg-primary-50">
                Get started free
                <ArrowRightIcon className="ml-2 h-4 w-4" />
              </Button>
            </Link>
            <Link href="/contact" className="text-sm font-semibold leading-6 text-white">
              Contact sales <span aria-hidden="true">→</span>
            </Link>
          </div>
          <div className="mt-8 text-sm text-primary-100">
            <p>No credit card required • 14-day free trial • Cancel anytime</p>
          </div>
        </div>
      </div>
    </div>
  )
}