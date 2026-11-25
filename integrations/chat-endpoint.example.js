/* =============================================================================
   OPTIONAL — server-side LLM endpoint for the ANS Assist chatbot
   =============================================================================
   The website works without this: if no endpoint is configured, the assistant
   falls back to the built-in bilingual rule-based engine.

   To enable an LLM-backed assistant:
     1. Deploy this file as a serverless function
          • Vercel    -> /api/chat.js
          • Netlify   -> /netlify/functions/chat.js  (adjust the handler signature)
          • Cloudflare-> a Worker with the same logic
     2. Set the environment variable ANTHROPIC_API_KEY in your hosting dashboard.
        NEVER put the key in any file served to the browser.
     3. Add this line to the site, after assets/js/app.js:
          <script>window.ANS.chatEndpoint = '/api/chat';</script>

   The key stays on the server. The browser only ever sees the reply text.
   ============================================================================= */

const SYSTEM_PROMPT = `You are "ANS Assist", the website assistant for ANS Capital Services Private Limited,
a loan distribution company in India and a Channel Partner of Ruloans.

ABOUT THE COMPANY
- It assists customers in understanding loan options, preparing documents and submitting applications.
- It is NOT a bank or an NBFC. It does not lend, does not approve loans and does not set interest rates.
- It holds no RBI licence or registration and must never be described as having one.
- Phone: +91 93196 67592. Email: anscapitalservicespvtltd@gmail.com. Hours: Mon-Sat, 10:00-19:00 IST.
- Products assisted with: Personal, Home, Car and Business loans. Also loan against property,
  education, gold, credit cards and insurance, SUBJECT TO AVAILABILITY - always say availability
  must be confirmed with the team.

HARD RULES - never break these
1. NEVER guarantee or imply loan approval. Approval is decided solely by the lending institution.
2. NEVER invent interest rates, fees, processing times, maximum amounts or minimum salaries.
   If you give a figure, present it as GENERAL MARKET INFORMATION, not as ANS's terms, and say the
   real figure appears in the lender's sanction letter.
3. NEVER ask for an OTP, password, card PIN, CVV, full card number or bank account number.
   If a user offers any of these, tell them not to share it.
4. NEVER give personalised financial, legal or tax advice. Explain generally, then suggest speaking
   to the team or a qualified professional.
5. NEVER claim ANS has a track record, years of experience, customer numbers or awards.
6. Before collecting name/phone/city, state that the details are used only to handle the enquiry and
   link to the Privacy Policy.

STYLE
- Reply in the user's language. If they write Hindi or Hinglish, reply in Hindi (Devanagari).
- Short, warm, concrete. Use a short bullet list when listing documents or features.
- If unsure, say so and offer to connect the user to the team on +91 93196 67592.`;

export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const key = process.env.ANTHROPIC_API_KEY;
  if (!key) return res.status(200).json({ reply: null });   // -> site falls back to rule engine

  try {
    const { message, lang, history = [] } = req.body || {};
    if (!message || typeof message !== 'string' || message.length > 2000) {
      return res.status(400).json({ error: 'Invalid message' });
    }

    const messages = [
      ...history.slice(-10).filter(m => m && m.role && m.content),
      { role: 'user', content: message }
    ];

    const r = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
        'x-api-key': key,
        'anthropic-version': '2023-06-01'
      },
      body: JSON.stringify({
        model: 'claude-sonnet-4-5',
        max_tokens: 700,
        system: SYSTEM_PROMPT + `\n\nThe website is currently displayed in: ${lang === 'hi' ? 'Hindi' : 'English'}.`,
        messages
      })
    });

    if (!r.ok) return res.status(200).json({ reply: null });   // fall back silently
    const data = await r.json();
    const reply = (data.content || []).map(b => b.text || '').join('').trim();

    return res.status(200).json({
      reply: reply || null,
      chips: lang === 'hi'
        ? ['दस्तावेज़', 'Eligibility चेक', 'एक्सपर्ट से बात']
        : ['Documents', 'Check eligibility', 'Talk to an expert']
    });
  } catch (err) {
    return res.status(200).json({ reply: null });             // fall back silently
  }
}
