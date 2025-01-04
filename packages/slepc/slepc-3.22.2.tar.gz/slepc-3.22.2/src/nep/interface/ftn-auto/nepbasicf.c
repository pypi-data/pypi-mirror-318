#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* nepbasic.c */
/* Fortran interface file */

/*
* This file was generated automatically by bfort from the C source
* file.  
 */

#ifdef PETSC_USE_POINTER_CONVERSION
#if defined(__cplusplus)
extern "C" { 
#endif 
extern void *PetscToPointer(void*);
extern int PetscFromPointer(void *);
extern void PetscRmPointer(void*);
#if defined(__cplusplus)
} 
#endif 

#else

#define PetscToPointer(a) (a ? *(PetscFortranAddr *)(a) : 0)
#define PetscFromPointer(a) (PetscFortranAddr)(a)
#define PetscRmPointer(a)
#endif

#include "slepcnep.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepcreate_ NEPCREATE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepcreate_ nepcreate
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepsettype_ NEPSETTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepsettype_ nepsettype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepgettype_ NEPGETTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepgettype_ nepgettype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepreset_ NEPRESET
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepreset_ nepreset
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepdestroy_ NEPDESTROY
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepdestroy_ nepdestroy
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepsetbv_ NEPSETBV
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepsetbv_ nepsetbv
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepgetbv_ NEPGETBV
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepgetbv_ nepgetbv
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepsetrg_ NEPSETRG
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepsetrg_ nepsetrg
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepgetrg_ NEPGETRG
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepgetrg_ nepgetrg
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepsetds_ NEPSETDS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepsetds_ nepsetds
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepgetds_ NEPGETDS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepgetds_ nepgetds
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define neprefinegetksp_ NEPREFINEGETKSP
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define neprefinegetksp_ neprefinegetksp
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepsettarget_ NEPSETTARGET
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepsettarget_ nepsettarget
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepgettarget_ NEPGETTARGET
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepgettarget_ nepgettarget
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepsetsplitoperator_ NEPSETSPLITOPERATOR
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepsetsplitoperator_ nepsetsplitoperator
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepgetsplitoperatorterm_ NEPGETSPLITOPERATORTERM
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepgetsplitoperatorterm_ nepgetsplitoperatorterm
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepgetsplitoperatorinfo_ NEPGETSPLITOPERATORINFO
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepgetsplitoperatorinfo_ nepgetsplitoperatorinfo
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepsetsplitpreconditioner_ NEPSETSPLITPRECONDITIONER
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepsetsplitpreconditioner_ nepsetsplitpreconditioner
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepgetsplitpreconditionerterm_ NEPGETSPLITPRECONDITIONERTERM
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepgetsplitpreconditionerterm_ nepgetsplitpreconditionerterm
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepgetsplitpreconditionerinfo_ NEPGETSPLITPRECONDITIONERINFO
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepgetsplitpreconditionerinfo_ nepgetsplitpreconditionerinfo
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  nepcreate_(MPI_Fint * comm,NEP *outnep, int *ierr)
{
PETSC_FORTRAN_OBJECT_CREATE(outnep);
 PetscBool outnep_null = !*(void**) outnep ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(outnep);
*ierr = NEPCreate(
	MPI_Comm_f2c(*(comm)),outnep);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! outnep_null && !*(void**) outnep) * (void **) outnep = (void *)-2;
}
SLEPC_EXTERN void  nepsettype_(NEP nep,char *type, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(nep);
/* insert Fortran-to-C conversion for type */
  FIXCHAR(type,cl0,_cltmp0);
*ierr = NEPSetType(
	(NEP)PetscToPointer((nep) ),_cltmp0);
  FREECHAR(type,_cltmp0);
}
SLEPC_EXTERN void  nepgettype_(NEP nep,char *type, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPGetType(
	(NEP)PetscToPointer((nep) ),(const char **)&_cltmp0);
/* insert C-to-Fortran conversion for type */
*ierr = PetscStrncpy(type, _cltmp0, cl0);
                        if (*ierr) return;
                        FIXRETURNCHAR(PETSC_TRUE, type, cl0);
}
SLEPC_EXTERN void  nepreset_(NEP nep, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPReset(
	(NEP)PetscToPointer((nep) ));
}
SLEPC_EXTERN void  nepdestroy_(NEP *nep, int *ierr)
{
PETSC_FORTRAN_OBJECT_F_DESTROYED_TO_C_NULL(nep);
 PetscBool nep_null = !*(void**) nep ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPDestroy(nep);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! nep_null && !*(void**) nep) * (void **) nep = (void *)-2;
if (*ierr) return;
PETSC_FORTRAN_OBJECT_C_NULL_TO_F_DESTROYED(nep);
 }
SLEPC_EXTERN void  nepsetbv_(NEP nep,BV bv, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLOBJECT(bv);
*ierr = NEPSetBV(
	(NEP)PetscToPointer((nep) ),
	(BV)PetscToPointer((bv) ));
}
SLEPC_EXTERN void  nepgetbv_(NEP nep,BV *bv, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
PetscBool bv_null = !*(void**) bv ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(bv);
*ierr = NEPGetBV(
	(NEP)PetscToPointer((nep) ),bv);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! bv_null && !*(void**) bv) * (void **) bv = (void *)-2;
}
SLEPC_EXTERN void  nepsetrg_(NEP nep,RG rg, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLOBJECT(rg);
*ierr = NEPSetRG(
	(NEP)PetscToPointer((nep) ),
	(RG)PetscToPointer((rg) ));
}
SLEPC_EXTERN void  nepgetrg_(NEP nep,RG *rg, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
PetscBool rg_null = !*(void**) rg ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(rg);
*ierr = NEPGetRG(
	(NEP)PetscToPointer((nep) ),rg);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! rg_null && !*(void**) rg) * (void **) rg = (void *)-2;
}
SLEPC_EXTERN void  nepsetds_(NEP nep,DS ds, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLOBJECT(ds);
*ierr = NEPSetDS(
	(NEP)PetscToPointer((nep) ),
	(DS)PetscToPointer((ds) ));
}
SLEPC_EXTERN void  nepgetds_(NEP nep,DS *ds, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
PetscBool ds_null = !*(void**) ds ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(ds);
*ierr = NEPGetDS(
	(NEP)PetscToPointer((nep) ),ds);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! ds_null && !*(void**) ds) * (void **) ds = (void *)-2;
}
SLEPC_EXTERN void  neprefinegetksp_(NEP nep,KSP *ksp, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
PetscBool ksp_null = !*(void**) ksp ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(ksp);
*ierr = NEPRefineGetKSP(
	(NEP)PetscToPointer((nep) ),ksp);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! ksp_null && !*(void**) ksp) * (void **) ksp = (void *)-2;
}
SLEPC_EXTERN void  nepsettarget_(NEP nep,PetscScalar *target, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPSetTarget(
	(NEP)PetscToPointer((nep) ),*target);
}
SLEPC_EXTERN void  nepgettarget_(NEP nep,PetscScalar* target, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLSCALAR(target);
*ierr = NEPGetTarget(
	(NEP)PetscToPointer((nep) ),target);
}
SLEPC_EXTERN void  nepsetsplitoperator_(NEP nep,PetscInt *nt,Mat A[],FN f[],MatStructure *str, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
PetscBool A_null = !*(void**) A ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(A);
PetscBool f_null = !*(void**) f ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(f);
*ierr = NEPSetSplitOperator(
	(NEP)PetscToPointer((nep) ),*nt,A,f,*str);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! A_null && !*(void**) A) * (void **) A = (void *)-2;
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! f_null && !*(void**) f) * (void **) f = (void *)-2;
}
SLEPC_EXTERN void  nepgetsplitoperatorterm_(NEP nep,PetscInt *k,Mat *A,FN *f, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
PetscBool A_null = !*(void**) A ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(A);
PetscBool f_null = !*(void**) f ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(f);
*ierr = NEPGetSplitOperatorTerm(
	(NEP)PetscToPointer((nep) ),*k,A,f);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! A_null && !*(void**) A) * (void **) A = (void *)-2;
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! f_null && !*(void**) f) * (void **) f = (void *)-2;
}
SLEPC_EXTERN void  nepgetsplitoperatorinfo_(NEP nep,PetscInt *n,MatStructure *str, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLINTEGER(n);
*ierr = NEPGetSplitOperatorInfo(
	(NEP)PetscToPointer((nep) ),n,str);
}
SLEPC_EXTERN void  nepsetsplitpreconditioner_(NEP nep,PetscInt *ntp,Mat P[],MatStructure *strp, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
PetscBool P_null = !*(void**) P ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(P);
*ierr = NEPSetSplitPreconditioner(
	(NEP)PetscToPointer((nep) ),*ntp,P,*strp);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! P_null && !*(void**) P) * (void **) P = (void *)-2;
}
SLEPC_EXTERN void  nepgetsplitpreconditionerterm_(NEP nep,PetscInt *k,Mat *P, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
PetscBool P_null = !*(void**) P ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(P);
*ierr = NEPGetSplitPreconditionerTerm(
	(NEP)PetscToPointer((nep) ),*k,P);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! P_null && !*(void**) P) * (void **) P = (void *)-2;
}
SLEPC_EXTERN void  nepgetsplitpreconditionerinfo_(NEP nep,PetscInt *n,MatStructure *strp, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLINTEGER(n);
*ierr = NEPGetSplitPreconditionerInfo(
	(NEP)PetscToPointer((nep) ),n,strp);
}
#if defined(__cplusplus)
}
#endif
