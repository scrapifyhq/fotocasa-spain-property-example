import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('scrapefy/fotocasa-property-scraper').call({
    locations: ['madrid-capital'],
    operation: 'buy',
    propertyType: 'homes',
    minPrice: 200000,
    maxPrice: 450000,
    minRooms: 2,
    maxAgeDays: 7,
    maxItems: 100,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items.length, 'listings');
