/**
 * PayEcho Firebase SDK & Backend Integration Client
 * Production integration for PayEcho.online
 * Project: upi-alert-6f4f3
 */

(function (window) {
  'use strict';

  // Firebase Web SDK Configuration
  const firebaseConfig = {
    apiKey: "AIzaSyAWDw0SAw4aQGyG76NwGX0MjwKWvqBL47o",
    authDomain: "upi-alert-6f4f3.firebaseapp.com",
    projectId: "upi-alert-6f4f3",
    storageBucket: "upi-alert-6f4f3.firebasestorage.app",
    messagingSenderId: "654711006924",
    appId: "1:654711006924:web:payecho-online"
  };

  // Safe initialize
  let app;
  if (!window.firebase) {
    console.warn("PayEcho: Firebase SDK not detected on window.");
  } else {
    try {
      app = !window.firebase.apps.length 
        ? window.firebase.initializeApp(firebaseConfig) 
        : window.firebase.app();
    } catch (e) {
      console.error("PayEcho: Firebase initialization error:", e);
    }
  }

  const auth = window.firebase ? window.firebase.auth() : null;
  const db = window.firebase ? window.firebase.firestore() : null;
  const functions = window.firebase ? window.firebase.functions() : null;

  // Plan catalog definition
  const PLAN_CATALOG = {
    free: {
      id: 'free',
      name: 'PayEcho Free Tier',
      price: 0,
      interval: 'None',
      features: ['Unlimited basic UPI voice alerts', 'All UPI apps (GPay, PhonePe, Paytm)', 'Standard TTS voice']
    },
    monthly: {
      id: 'monthly',
      name: 'PayEcho Pro Monthly',
      price: 99,
      interval: 'Monthly',
      features: ['Custom voice templates', 'High-volume voice booster', 'All regional Indian languages', 'No ads or banners', 'Priority support']
    },
    yearly: {
      id: 'yearly',
      name: 'PayEcho Business Yearly',
      price: 899,
      interval: 'Yearly',
      features: ['Multi-device store team mode', 'Cashier sub-accounts', 'Daily transaction CSV export', 'All Pro features included']
    },
    business: {
      id: 'business',
      name: 'PayEcho Business',
      price: 199,
      interval: 'Monthly',
      features: ['Multi-counter voice broadcasting', 'Team management', 'Priority WhatsApp support']
    },
    lifetime: {
      id: 'lifetime',
      name: 'PayEcho Lifetime Access',
      price: 499,
      interval: 'Lifetime One-Time',
      features: ['Permanent unlimited access', 'Never pay monthly soundbox rent', 'All future Pro updates included']
    }
  };

  // Authentication Helpers
  const PayEchoAuth = {
    currentUser: null,
    
    init(callback) {
      if (!auth) {
        if (callback) callback(null);
        return;
      }
      auth.onAuthStateChanged(function (user) {
        PayEchoAuth.currentUser = user;
        if (callback) callback(user);
      });
    },

    signInWithGoogle() {
      if (!auth) return Promise.reject(new Error("Firebase Auth not initialized"));
      const provider = new window.firebase.auth.GoogleAuthProvider();
      provider.addScope('email');
      provider.addScope('profile');
      return auth.signInWithPopup(provider);
    },

    signInWithEmail(email, password) {
      if (!auth) return Promise.reject(new Error("Firebase Auth not initialized"));
      return auth.signInWithEmailAndPassword(email, password);
    },

    signUpWithEmail(email, password, displayName) {
      if (!auth) return Promise.reject(new Error("Firebase Auth not initialized"));
      return auth.createUserWithEmailAndPassword(email, password).then(function (userCred) {
        if (displayName && userCred.user) {
          return userCred.user.updateProfile({ displayName: displayName }).then(function () {
            return PayEchoAPI.ensureUserDocument(userCred.user).then(function () {
              return userCred;
            });
          });
        }
        return PayEchoAPI.ensureUserDocument(userCred.user).then(function () {
          return userCred;
        });
      });
    },

    sendPasswordReset(email) {
      if (!auth) return Promise.reject(new Error("Firebase Auth not initialized"));
      return auth.sendPasswordResetEmail(email);
    },

    signOut() {
      if (!auth) return Promise.resolve();
      return auth.signOut();
    }
  };

  // Data & Backend API operations
  const PayEchoAPI = {
    ensureUserDocument(user) {
      if (!db || !user) return Promise.resolve();
      const userRef = db.collection('users').doc(user.uid);
      return userRef.get().then(function (docSnap) {
        if (!docSnap.exists) {
          const now = window.firebase.firestore.FieldValue.serverTimestamp();
          return userRef.set({
            name: user.displayName || 'Shop Owner',
            email: user.email || '',
            isPremium: false,
            planType: 'free',
            subscriptionStatus: 'free',
            createdAt: now,
            lastLogin: now,
            language: 'hi'
          }, { merge: true });
        }
      }).catch(function (err) {
        console.warn("ensureUserDocument notice:", err);
      });
    },

    getUserSubscription(uid) {
      if (!db || !uid) return Promise.reject(new Error("Database not available"));
      return db.collection('users').doc(uid).get().then(function (docSnap) {
        if (!docSnap.exists) {
          return {
            uid: uid,
            isPremium: false,
            planType: 'free',
            planName: PLAN_CATALOG.free.name,
            price: 0,
            interval: 'None',
            status: 'free',
            statusDisplay: 'Free Plan',
            provider: 'none',
            providerDisplay: 'None',
            expiryDate: null,
            startDate: null,
            latestOrderId: null,
            isPlayStore: false,
            isAlternativeBilling: false,
            cancelledAt: null
          };
        }

        const data = docSnap.data();
        const planKey = (data.planType || 'free').toLowerCase();
        const planInfo = PLAN_CATALOG[planKey] || {
          id: planKey,
          name: data.planName || (planKey.charAt(0).toUpperCase() + planKey.slice(1) + ' Plan'),
          price: data.revenueAmount || (planKey === 'yearly' ? 899 : (planKey === 'lifetime' ? 499 : 99)),
          interval: planKey === 'lifetime' ? 'Lifetime One-Time' : (planKey === 'yearly' ? 'Yearly' : 'Monthly'),
          features: []
        };

        let expiryDate = null;
        if (data.premiumExpiry && typeof data.premiumExpiry.toDate === 'function') {
          expiryDate = data.premiumExpiry.toDate();
        } else if (data.premiumExpiry) {
          expiryDate = new Date(data.premiumExpiry);
        }

        let startDate = null;
        if (data.premiumStart && typeof data.premiumStart.toDate === 'function') {
          startDate = data.premiumStart.toDate();
        } else if (data.createdAt && typeof data.createdAt.toDate === 'function') {
          startDate = data.createdAt.toDate();
        }

        let cancelledAt = null;
        if (data.subscriptionCancelledAt && typeof data.subscriptionCancelledAt.toDate === 'function') {
          cancelledAt = data.subscriptionCancelledAt.toDate();
        }

        const rawStatus = (data.subscriptionStatus || (data.isPremium ? 'active' : 'free')).toLowerCase();
        
        let status = rawStatus;
        const now = new Date();
        if (expiryDate && expiryDate < now && status !== 'lifetime') {
          status = 'expired';
        }

        let statusDisplay = 'Active';
        if (status === 'cancelled') {
          statusDisplay = expiryDate && expiryDate > now 
            ? 'Cancelled (Active until ' + expiryDate.toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' }) + ')'
            : 'Cancelled';
        } else if (status === 'on_hold' || status === 'payment_failed') {
          statusDisplay = 'Payment On Hold';
        } else if (status === 'expired') {
          statusDisplay = 'Expired';
        } else if (status === 'lifetime') {
          statusDisplay = 'Lifetime Access';
        } else if (status === 'free') {
          statusDisplay = 'Free Plan';
        }

        // Determine billing provider
        let provider = data.billingProvider || 'google_play';
        if (data.latestOrderId && data.latestOrderId.startsWith('order_')) {
          provider = 'razorpay';
        } else if (data.latestOrderId && data.latestOrderId.startsWith('GPA.')) {
          provider = 'google_play';
        } else if (data.razorpayPaymentId || data.razorpaySubscriptionId) {
          provider = 'razorpay';
        }

        const isPlayStore = provider === 'google_play';
        const isAlternativeBilling = provider === 'razorpay' || provider === 'alternative_billing';
        const providerDisplay = isPlayStore ? 'Google Play Store' : (isAlternativeBilling ? 'Alternative Billing (Razorpay)' : 'Direct Web');

        return {
          uid: uid,
          email: data.email || (auth.currentUser ? auth.currentUser.email : ''),
          name: data.name || (auth.currentUser ? auth.currentUser.displayName : 'Shop Owner'),
          isPremium: !!data.isPremium && status !== 'expired',
          planType: planKey,
          planName: planInfo.name,
          price: planInfo.price,
          interval: planInfo.interval,
          status: status,
          statusDisplay: statusDisplay,
          provider: provider,
          providerDisplay: providerDisplay,
          isPlayStore: isPlayStore,
          isAlternativeBilling: isAlternativeBilling,
          expiryDate: expiryDate,
          startDate: startDate,
          cancelledAt: cancelledAt,
          latestOrderId: data.latestOrderId || (isPlayStore && data.isPremium ? 'GPA.AUTO-SYNC-' + uid.substring(0, 6) : null),
          purchaseToken: data.latestPurchaseToken || null,
          features: planInfo.features
        };
      });
    },

    getUserOrders(uid) {
      if (!db || !uid) return Promise.reject(new Error("Database not available"));
      
      const ordersList = [];
      const userRef = db.collection('users').doc(uid);

      // 1. Fetch from users/{uid}/orders subcollection
      const p1 = userRef.collection('orders').orderBy('createdAt', 'desc').get().catch(function () {
        return { empty: true, docs: [] };
      });

      // 2. Fetch from root orders collection where userId == uid
      const p2 = db.collection('orders').where('userId', '==', uid).get().catch(function () {
        return { empty: true, docs: [] };
      });

      // 3. Fetch user profile doc to include root order ID if not stored in subcollection
      const p3 = userRef.get().catch(function () { return { exists: false }; });

      return Promise.all([p1, p2, p3]).then(function (results) {
        const subSnap = results[0];
        const rootSnap = results[1];
        const userDocSnap = results[2];

        const seenOrderIds = new Set();

        function addOrder(docData, id) {
          const oid = docData.orderId || docData.latestOrderId || id;
          if (seenOrderIds.has(oid)) return;
          seenOrderIds.add(oid);

          let createdAt = new Date();
          if (docData.createdAt && typeof docData.createdAt.toDate === 'function') {
            createdAt = docData.createdAt.toDate();
          } else if (docData.createdAt) {
            createdAt = new Date(docData.createdAt);
          } else if (docData.timestamp && typeof docData.timestamp.toDate === 'function') {
            createdAt = docData.timestamp.toDate();
          }

          let provider = docData.provider || 'google_play';
          if (oid.startsWith('order_') || docData.razorpayPaymentId) {
            provider = 'razorpay';
          } else if (oid.startsWith('GPA.')) {
            provider = 'google_play';
          }

          ordersList.push({
            id: id,
            orderId: oid,
            amount: docData.amount || docData.revenueAmount || 99,
            currency: docData.currency || 'INR',
            status: docData.status || (docData.subscriptionStatus === 'cancelled' ? 'paid' : (docData.isPremium ? 'paid' : 'completed')),
            provider: provider,
            providerDisplay: provider === 'google_play' ? 'Google Play Store' : 'Razorpay (Alternative Billing)',
            planName: docData.planName || (docData.planType ? (PLAN_CATALOG[docData.planType] ? PLAN_CATALOG[docData.planType].name : docData.planType) : 'PayEcho Pro Monthly'),
            planType: docData.planType || 'monthly',
            createdAt: createdAt,
            razorpayPaymentId: docData.razorpayPaymentId || null,
            razorpayOrderId: docData.razorpayOrderId || null,
            receiptUrl: docData.receiptUrl || null
          });
        }

        if (subSnap && !subSnap.empty) {
          subSnap.docs.forEach(function (d) { addOrder(d.data(), d.id); });
        }
        if (rootSnap && !rootSnap.empty) {
          rootSnap.docs.forEach(function (d) { addOrder(d.data(), d.id); });
        }

        if (userDocSnap && userDocSnap.exists) {
          const udata = userDocSnap.data();
          if (udata.latestOrderId && !seenOrderIds.has(udata.latestOrderId)) {
            const planKey = (udata.planType || 'monthly').toLowerCase();
            const planInfo = PLAN_CATALOG[planKey] || PLAN_CATALOG.monthly;
            let date = new Date();
            if (udata.premiumStart && typeof udata.premiumStart.toDate === 'function') {
              date = udata.premiumStart.toDate();
            } else if (udata.createdAt && typeof udata.createdAt.toDate === 'function') {
              date = udata.createdAt.toDate();
            }
            addOrder({
              orderId: udata.latestOrderId,
              amount: planInfo.price,
              currency: 'INR',
              status: udata.subscriptionStatus === 'refunded' ? 'refunded' : 'paid',
              provider: udata.latestOrderId.startsWith('GPA.') ? 'google_play' : (udata.billingProvider || 'google_play'),
              planName: planInfo.name,
              planType: planKey,
              createdAt: date
            }, udata.latestOrderId);
          }
        }

        ordersList.sort(function (a, b) {
          return b.createdAt.getTime() - a.createdAt.getTime();
        });

        return ordersList;
      });
    },

    cancelSubscription(uid, reason, isPlayStore) {
      if (!uid) return Promise.reject(new Error("User ID is required"));

      // 1. Google Play Subscription:
      // Policy strictly prohibits cancelling Play Store subscriptions via client DB writes.
      // Direct the user to Google Play Subscriptions management.
      if (isPlayStore) {
        if (db) {
          db.collection('cancellation_feedback').add({
            userId: uid,
            provider: 'google_play',
            reason: reason || 'Not specified',
            createdAt: window.firebase.firestore.FieldValue.serverTimestamp()
          }).catch(function () {});
        }
        return Promise.resolve({
          success: false,
          isPlayStore: true,
          playStoreUrl: "https://play.google.com/store/account/subscriptions?package=com.bhava.upialert",
          message: "Google Play subscriptions must be cancelled through your Google Play account to stop future bank deductions."
        });
      }

      // 2. Razorpay / Alternative Billing Subscription:
      // Must be cancelled through secure backend Cloud Function calling Razorpay API.
      if (functions) {
        try {
          const fn = functions.httpsCallable('cancelSubscription');
          return fn({ reason: reason || 'User requested cancellation' })
            .then(function (res) { return res.data; });
        } catch (e) {
          return Promise.reject(new Error("Backend cancellation service is unavailable. Please email support@payecho.online."));
        }
      }

      return Promise.reject(new Error("Backend cancellation service is unavailable. Please email support@payecho.online."));
    },

    createRazorpayOrder(planType) {
      if (!functions) return Promise.reject(new Error("Firebase Functions not available"));
      const fn = functions.httpsCallable('createRazorpayOrder');
      return fn({ planType: planType }).then(function (res) { return res.data; });
    },

    verifyRazorpayPayment(paymentData) {
      if (!functions) return Promise.reject(new Error("Firebase Functions not available"));
      const fn = functions.httpsCallable('verifyRazorpayPayment');
      return fn(paymentData).then(function (res) { return res.data; });
    },

    requestRefund(refundData) {
      if (!refundData || !refundData.orderId) {
        return Promise.reject(new Error("Order ID is required for refund request"));
      }

      // Call Cloud Function to validate ownership and create pending request
      if (functions) {
        try {
          const fn = functions.httpsCallable('requestRefund');
          return fn(refundData)
            .then(function (res) { return res.data; })
            .catch(function (fnErr) {
              console.warn("Cloud function requestRefund failed, falling back to secure Firestore rules:", fnErr);
              return PayEchoAPI._requestRefundDirect(refundData);
            });
        } catch (e) {
          return PayEchoAPI._requestRefundDirect(refundData);
        }
      }

      return PayEchoAPI._requestRefundDirect(refundData);
    },

    _requestRefundDirect(refundData) {
      if (!db) return Promise.reject(new Error("Database not connected"));
      const now = window.firebase.firestore.FieldValue.serverTimestamp();
      const payload = {
        userId: refundData.uid || (auth.currentUser ? auth.currentUser.uid : null),
        userEmail: refundData.userEmail || (auth.currentUser ? auth.currentUser.email : ''),
        userName: refundData.userName || (auth.currentUser ? auth.currentUser.displayName : 'Customer'),
        orderId: refundData.orderId,
        amount: refundData.amount || null,
        reason: refundData.reason || 'Other',
        description: refundData.description || '',
        provider: refundData.provider || 'google_play',
        status: 'pending_review',
        createdAt: now,
        updatedAt: now
      };

      return db.collection('refund_requests').add(payload).then(function (docRef) {
        return {
          success: true,
          requestId: docRef.id,
          message: "Refund request submitted successfully. Our billing operations team will review your request within 3-5 business days."
        };
      });
    },

    getUserRefundRequests(uid) {
      if (!db || !uid) return Promise.resolve([]);
      return db.collection('refund_requests')
        .where('userId', '==', uid)
        .get()
        .then(function (snap) {
          const requests = [];
          snap.forEach(function (doc) {
            const d = doc.data();
            let date = new Date();
            if (d.createdAt && typeof d.createdAt.toDate === 'function') {
              date = d.createdAt.toDate();
            } else if (d.createdAt) {
              date = new Date(d.createdAt);
            }
            requests.push({
              id: doc.id,
              orderId: d.orderId,
              amount: d.amount,
              reason: d.reason,
              description: d.description,
              status: d.status || 'pending_review',
              adminNotes: d.adminNotes || null,
              createdAt: date
            });
          });
          requests.sort(function (a, b) { return b.createdAt.getTime() - a.createdAt.getTime(); });
          return requests;
        }).catch(function (err) {
          console.warn("getUserRefundRequests notice:", err);
          return [];
        });
    },

    submitSupportTicket(ticketData) {
      if (!ticketData || !ticketData.message || !ticketData.email) {
        return Promise.reject(new Error("Email and message are required"));
      }

      if (functions) {
        try {
          const fn = functions.httpsCallable('createSupportTicket');
          return fn(ticketData)
            .then(function (res) { return res.data; })
            .catch(function () {
              return PayEchoAPI._submitSupportTicketDirect(ticketData);
            });
        } catch (e) {
          return PayEchoAPI._submitSupportTicketDirect(ticketData);
        }
      }

      return PayEchoAPI._submitSupportTicketDirect(ticketData);
    },

    _submitSupportTicketDirect(ticketData) {
      if (!db) return Promise.reject(new Error("Database not connected"));
      const now = window.firebase.firestore.FieldValue.serverTimestamp();
      const payload = {
        userId: ticketData.uid || (auth.currentUser ? auth.currentUser.uid : 'guest'),
        userEmail: ticketData.email,
        userName: ticketData.name || 'Anonymous',
        category: ticketData.category || 'general',
        orderId: ticketData.orderId || null,
        subject: ticketData.subject || 'Support Request',
        message: ticketData.message,
        status: 'open',
        createdAt: now
      };

      return db.collection('support_tickets').add(payload).then(function (docRef) {
        return {
          success: true,
          ticketId: docRef.id,
          message: "Support ticket #" + docRef.id.substring(0, 8) + " created. Our team will contact you at " + ticketData.email + "."
        };
      });
    }
  };

  window.PayEchoAuth = PayEchoAuth;
  window.PayEchoAPI = PayEchoAPI;
  window.PLAN_CATALOG = PLAN_CATALOG;

})(window);
